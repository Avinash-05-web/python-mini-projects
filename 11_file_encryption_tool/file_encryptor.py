import argparse
import getpass
import os
import secrets
import struct
import sys
from pathlib import Path

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


# ============================================================
# Configuration
# ============================================================

MAGIC = b"PYENC001"
VERSION = 1

SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32

# 1 MiB chunks keep memory usage reasonable for large files.
CHUNK_SIZE = 1024 * 1024

# Scrypt parameters.
# These are intentionally expensive enough to make password
# guessing harder while remaining practical for a local tool.
SCRYPT_N = 2**15
SCRYPT_R = 8
SCRYPT_P = 1

# Each encrypted chunk contains:
#
#   4 bytes  -> plaintext length
#   16 bytes -> AES-GCM authentication tag
#
# The actual ciphertext is therefore:
#
#   4 + plaintext_length + 16
#
# Header format:
#
# MAGIC
# VERSION
# SALT
# BASE NONCE
# ORIGINAL FILE SIZE
# CHUNK SIZE
#
HEADER_FORMAT = "!8sB16s12sQQ"
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)


# ============================================================
# Utility Functions
# ============================================================

def secure_file_permissions(path):
    """
    Restrict file permissions on Unix-like systems.

    Windows permission semantics are different, so chmod is
    only attempted on non-Windows systems.
    """

    if os.name != "nt":
        try:
            os.chmod(path, 0o600)
        except OSError:
            pass


def derive_key(password, salt):
    """
    Derive a 256-bit encryption key from the password using Scrypt.
    """

    kdf = Scrypt(
        salt=salt,
        length=KEY_SIZE,
        n=SCRYPT_N,
        r=SCRYPT_R,
        p=SCRYPT_P,
    )

    return kdf.derive(password.encode("utf-8"))


def generate_output_path(input_path, decrypt=False):
    """
    Generate a safe default output filename.
    """

    if decrypt:
        if input_path.suffix == ".enc":
            return input_path.with_suffix("")

        return input_path.with_name(
            input_path.name + ".decrypted"
        )

    return input_path.with_name(
        input_path.name + ".enc"
    )


def confirm_overwrite(path):
    """
    Ask before overwriting an existing file.
    """

    if not path.exists():
        return True

    answer = input(
        f"⚠️ Output file already exists:\n"
        f"   {path}\n\n"
        f"Overwrite it? [y/N]: "
    ).strip().lower()

    return answer == "y"


def secure_password(prompt):
    """
    Read a password without displaying it on screen.
    """

    while True:
        password = getpass.getpass(prompt)

        if not password:
            print("❌ Password cannot be empty.")
            continue

        if len(password) < 8:
            print(
                "❌ Password must contain at least 8 characters."
            )
            continue

        return password


def get_encryption_password():
    """
    Request and confirm the encryption password.
    """

    while True:
        password = secure_password(
            "Enter encryption password: "
        )

        confirmation = getpass.getpass(
            "Confirm encryption password: "
        )

        if password != confirmation:
            print("❌ Passwords do not match.\n")
            continue

        return password


def show_progress(processed, total):
    """
    Display simple progress information.
    """

    if total <= 0:
        print("\rProgress: 100.00%", end="", flush=True)
        return

    percentage = (processed / total) * 100

    if percentage > 100:
        percentage = 100

    print(
        f"\rProgress: {percentage:6.2f}%",
        end="",
        flush=True,
    )


# ============================================================
# Nonce Management
# ============================================================

def make_chunk_nonce(base_nonce, counter):
    """
    Create a unique 96-bit nonce for each chunk.

    The first 4 bytes are the random base nonce.
    The last 8 bytes contain the chunk counter.

    Because the counter never repeats for a given file,
    each AES-GCM encryption gets a unique nonce.
    """

    if counter < 0 or counter >= 2**64:
        raise ValueError("Chunk counter exceeded safe limit.")

    return base_nonce[:4] + counter.to_bytes(8, "big")


# ============================================================
# Encryption
# ============================================================

def encrypt_file(input_path, output_path, password):
    """
    Encrypt a file using:

        Scrypt
          ↓
        256-bit key
          ↓
        AES-256-GCM
          ↓
        Chunked authenticated encryption
    """

    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.is_file():
        raise FileNotFoundError(
            f"Input file does not exist: {input_path}"
        )

    if input_path.resolve() == output_path.resolve():
        raise ValueError(
            "Input and output files must be different."
        )

    file_size = input_path.stat().st_size

    salt = secrets.token_bytes(SALT_SIZE)
    base_nonce = secrets.token_bytes(NONCE_SIZE)

    key = derive_key(password, salt)
    cipher = AESGCM(key)

    # Header is authenticated as additional data.
    header = struct.pack(
        HEADER_FORMAT,
        MAGIC,
        VERSION,
        salt,
        base_nonce,
        file_size,
        CHUNK_SIZE,
    )

    temp_path = output_path.with_name(
        output_path.name + ".tmp"
    )

    processed = 0
    chunk_counter = 0

    try:
        with open(input_path, "rb") as source, open(
            temp_path, "wb"
        ) as destination:

            destination.write(header)

            while True:
                chunk = source.read(CHUNK_SIZE)

                if not chunk:
                    break

                nonce = make_chunk_nonce(
                    base_nonce,
                    chunk_counter,
                )

                # Encrypt chunk and authenticate header.
                encrypted_chunk = cipher.encrypt(
                    nonce,
                    chunk,
                    header,
                )

                # Store plaintext length before ciphertext.
                destination.write(
                    struct.pack("!I", len(chunk))
                )

                destination.write(encrypted_chunk)

                processed += len(chunk)
                chunk_counter += 1

                show_progress(
                    processed,
                    file_size,
                )

        secure_file_permissions(temp_path)

        # Atomic replacement after successful encryption.
        os.replace(temp_path, output_path)

        print("\n")
        print("✅ Encryption completed.")
        print(f"📄 Input : {input_path}")
        print(f"🔐 Output: {output_path}")
        print(f"📦 Size  : {file_size:,} bytes")
        print(
            "🔑 Your password is NOT stored in the encrypted file."
        )

    except Exception:
        try:
            if temp_path.exists():
                temp_path.unlink()
        except OSError:
            pass

        raise


# ============================================================
# Decryption
# ============================================================

def read_header(file):
    """
    Read and validate the encrypted file header.
    """

    raw_header = file.read(HEADER_SIZE)

    if len(raw_header) != HEADER_SIZE:
        raise ValueError(
            "Encrypted file is incomplete or corrupted."
        )

    (
        magic,
        version,
        salt,
        base_nonce,
        original_size,
        chunk_size,
    ) = struct.unpack(
        HEADER_FORMAT,
        raw_header,
    )

    if magic != MAGIC:
        raise ValueError(
            "This does not appear to be a supported encrypted file."
        )

    if version != VERSION:
        raise ValueError(
            f"Unsupported encryption format version: {version}"
        )

    if chunk_size <= 0 or chunk_size > 64 * 1024 * 1024:
        raise ValueError(
            "Invalid encrypted chunk size."
        )

    return (
        raw_header,
        salt,
        base_nonce,
        original_size,
        chunk_size,
    )


def decrypt_file(input_path, output_path, password):
    """
    Decrypt and authenticate an encrypted file.
    """

    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.is_file():
        raise FileNotFoundError(
            f"Encrypted file does not exist: {input_path}"
        )

    if input_path.resolve() == output_path.resolve():
        raise ValueError(
            "Input and output files must be different."
        )

    temp_path = output_path.with_name(
        output_path.name + ".tmp"
    )

    processed = 0
    chunk_counter = 0

    try:
        with open(input_path, "rb") as source:

            (
                header,
                salt,
                base_nonce,
                original_size,
                chunk_size,
            ) = read_header(source)

            key = derive_key(password, salt)
            cipher = AESGCM(key)

            with open(temp_path, "wb") as destination:

                while processed < original_size:

                    length_data = source.read(4)

                    if len(length_data) != 4:
                        raise ValueError(
                            "Encrypted file is truncated."
                        )

                    plaintext_length = struct.unpack(
                        "!I",
                        length_data,
                    )[0]

                    if plaintext_length == 0:
                        raise ValueError(
                            "Invalid encrypted chunk length."
                        )

                    if plaintext_length > chunk_size:
                        raise ValueError(
                            "Encrypted chunk exceeds declared size."
                        )

                    # AES-GCM adds a 16-byte authentication tag.
                    ciphertext_length = (
                        plaintext_length + 16
                    )

                    encrypted_chunk = source.read(
                        ciphertext_length
                    )

                    if len(encrypted_chunk) != ciphertext_length:
                        raise ValueError(
                            "Encrypted file is truncated."
                        )

                    nonce = make_chunk_nonce(
                        base_nonce,
                        chunk_counter,
                    )

                    try:
                        plaintext = cipher.decrypt(
                            nonce,
                            encrypted_chunk,
                            header,
                        )

                    except InvalidTag:
                        raise ValueError(
                            "Authentication failed. "
                            "The password may be incorrect, "
                            "or the encrypted file may have "
                            "been modified or corrupted."
                        )

                    if len(plaintext) != plaintext_length:
                        raise ValueError(
                            "Decrypted chunk size is invalid."
                        )

                    destination.write(plaintext)

                    processed += len(plaintext)
                    chunk_counter += 1

                    show_progress(
                        processed,
                        original_size,
                    )

                # There should be no unexpected trailing data.
                if source.read(1):
                    raise ValueError(
                        "Encrypted file contains unexpected trailing data."
                    )

        if processed != original_size:
            raise ValueError(
                "Decrypted file size does not match metadata."
            )

        secure_file_permissions(temp_path)

        # Replace only after the complete file has been
        # successfully authenticated and written.
        os.replace(temp_path, output_path)

        print("\n")
        print("✅ Decryption completed.")
        print(f"🔐 Input : {input_path}")
        print(f"📄 Output: {output_path}")
        print(f"📦 Size  : {processed:,} bytes")

    except Exception:
        try:
            if temp_path.exists():
                temp_path.unlink()
        except OSError:
            pass

        raise


# ============================================================
# Password Handling
# ============================================================

def ask_for_password(decrypt=False):
    """
    Ask for the appropriate password.
    """

    if decrypt:
        while True:
            password = getpass.getpass(
                "Enter decryption password: "
            )

            if password:
                return password

            print("❌ Password cannot be empty.")

    return get_encryption_password()


# ============================================================
# CLI
# ============================================================

def create_parser():
    """
    Create the command-line argument parser.
    """

    parser = argparse.ArgumentParser(
        description=(
            "Securely encrypt or decrypt files using "
            "Scrypt and AES-256-GCM."
        )
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    # Encryption command
    encrypt_parser = subparsers.add_parser(
        "encrypt",
        help="Encrypt a file.",
    )

    encrypt_parser.add_argument(
        "input",
        help="Path to the file to encrypt.",
    )

    encrypt_parser.add_argument(
        "-o",
        "--output",
        help="Output encrypted file path.",
    )

    # Decryption command
    decrypt_parser = subparsers.add_parser(
        "decrypt",
        help="Decrypt an encrypted file.",
    )

    decrypt_parser.add_argument(
        "input",
        help="Path to the encrypted file.",
    )

    decrypt_parser.add_argument(
        "-o",
        "--output",
        help="Output decrypted file path.",
    )

    return parser


# ============================================================
# Main
# ============================================================

def main():
    parser = create_parser()
    args = parser.parse_args()

    input_path = Path(args.input)

    if args.command == "encrypt":

        output_path = (
            Path(args.output)
            if args.output
            else generate_output_path(
                input_path,
                decrypt=False,
            )
        )

        if not input_path.is_file():
            print(
                f"❌ File not found: {input_path}"
            )
            return 1

        if not confirm_overwrite(output_path):
            print("❌ Operation cancelled.")
            return 0

        try:
            password = ask_for_password(
                decrypt=False
            )

            print("\n🔐 Starting encryption...")
            print(
                "⚠️ Keep your password safe. "
                "It cannot be recovered by this program.\n"
            )

            encrypt_file(
                input_path,
                output_path,
                password,
            )

        except KeyboardInterrupt:
            print("\n\n⚠️ Operation cancelled.")
            return 130

        except (OSError, ValueError) as error:
            print(f"\n❌ Error: {error}")
            return 1

        return 0

    if args.command == "decrypt":

        output_path = (
            Path(args.output)
            if args.output
            else generate_output_path(
                input_path,
                decrypt=True,
            )
        )

        if not input_path.is_file():
            print(
                f"❌ File not found: {input_path}"
            )
            return 1

        if not confirm_overwrite(output_path):
            print("❌ Operation cancelled.")
            return 0

        try:
            password = ask_for_password(
                decrypt=True
            )

            print("\n🔓 Starting decryption...\n")

            decrypt_file(
                input_path,
                output_path,
                password,
            )

        except KeyboardInterrupt:
            print("\n\n⚠️ Operation cancelled.")
            return 130

        except (OSError, ValueError) as error:
            print(f"\n❌ Error: {error}")
            return 1

        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())

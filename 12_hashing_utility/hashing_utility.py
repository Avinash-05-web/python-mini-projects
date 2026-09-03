#!/usr/bin/env python3

"""
Hashing Utility
---------------
Generate and verify cryptographic hashes for files and directories.

Features:
- SHA-256, SHA-512, SHA-1, MD5
- Chunked hashing for large files
- Single-file hash generation
- Hash verification
- Directory manifest generation
- Manifest verification
- Multiple files
- Progress display
- Human-readable file sizes
- Safe error handling
- Standard library only
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path
from typing import Iterable


# ============================================================
# Configuration
# ============================================================

DEFAULT_ALGORITHM = "sha256"
DEFAULT_CHUNK_SIZE = 1024 * 1024  # 1 MiB

SUPPORTED_ALGORITHMS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
}


# ============================================================
# Utility Functions
# ============================================================

def format_size(size: int) -> str:
    """Convert bytes into a human-readable size."""

    units = ["B", "KB", "MB", "GB", "TB", "PB"]

    value = float(size)

    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.2f} {unit}"

        value /= 1024

    return f"{size} B"


def get_algorithm(name: str):
    """Return the hashlib constructor for the selected algorithm."""

    name = name.lower()

    if name not in SUPPORTED_ALGORITHMS:
        supported = ", ".join(SUPPORTED_ALGORITHMS.keys())

        raise ValueError(
            f"Unsupported algorithm '{name}'. "
            f"Supported algorithms: {supported}"
        )

    return SUPPORTED_ALGORITHMS[name]


def normalize_hash(value: str) -> str:
    """Normalize a hash value for comparison."""

    return value.strip().lower()


def validate_hash(expected_hash: str, algorithm: str) -> bool:
    """Validate the expected hash format."""

    expected_hash = normalize_hash(expected_hash)

    expected_length = get_algorithm(algorithm)().digest_size * 2

    if len(expected_hash) != expected_length:
        return False

    try:
        int(expected_hash, 16)
    except ValueError:
        return False

    return True


# ============================================================
# File Hashing
# ============================================================

def calculate_file_hash(
    file_path: Path,
    algorithm: str = DEFAULT_ALGORITHM,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
) -> tuple[str, int]:
    """
    Calculate a file hash using chunked reading.

    Returns:
        tuple[str, int]:
            Hash value and total bytes processed.
    """

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    if not file_path.is_file():
        raise ValueError(
            f"Not a regular file: {file_path}"
        )

    if chunk_size <= 0:
        raise ValueError(
            "Chunk size must be greater than zero."
        )

    hash_constructor = get_algorithm(algorithm)

    hasher = hash_constructor()

    total_bytes = 0

    with file_path.open("rb") as file:
        while True:
            chunk = file.read(chunk_size)

            if not chunk:
                break

            hasher.update(chunk)

            total_bytes += len(chunk)

    return hasher.hexdigest(), total_bytes


# ============================================================
# Progress Display
# ============================================================

def calculate_file_hash_with_progress(
    file_path: Path,
    algorithm: str,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
) -> tuple[str, int]:
    """
    Calculate a file hash while displaying progress.
    """

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    if not file_path.is_file():
        raise ValueError(
            f"Not a regular file: {file_path}"
        )

    if chunk_size <= 0:
        raise ValueError(
            "Chunk size must be greater than zero."
        )

    hash_constructor = get_algorithm(algorithm)

    hasher = hash_constructor()

    total_size = file_path.stat().st_size
    processed = 0

    with file_path.open("rb") as file:

        while True:

            chunk = file.read(chunk_size)

            if not chunk:
                break

            hasher.update(chunk)

            processed += len(chunk)

            if total_size > 0:
                percentage = (processed / total_size) * 100
            else:
                percentage = 100

            print(
                f"\rProgress: {percentage:6.2f}% "
                f"({format_size(processed)} / "
                f"{format_size(total_size)})",
                end="",
                flush=True,
            )

    print()

    return hasher.hexdigest(), processed


# ============================================================
# Single File Hash
# ============================================================

def hash_command(args: argparse.Namespace) -> int:
    """Handle the hash command."""

    files = [Path(file) for file in args.files]

    for index, file_path in enumerate(files):

        if len(files) > 1:
            print(
                f"\n[{index + 1}/{len(files)}] "
                f"{file_path}"
            )

        try:

            if args.progress:

                digest, total_bytes = (
                    calculate_file_hash_with_progress(
                        file_path,
                        args.algorithm,
                        args.chunk_size,
                    )
                )

            else:

                digest, total_bytes = calculate_file_hash(
                    file_path,
                    args.algorithm,
                    args.chunk_size,
                )

            print(f"File:      {file_path}")
            print(f"Algorithm: {args.algorithm.upper()}")
            print(f"Size:      {format_size(total_bytes)}")
            print(f"Hash:      {digest}")

        except (FileNotFoundError, PermissionError, ValueError) as error:

            print(
                f"Error: {error}",
                file=sys.stderr,
            )

            if len(files) == 1:
                return 1

    return 0


# ============================================================
# Hash Verification
# ============================================================

def verify_command(args: argparse.Namespace) -> int:
    """Verify a file against an expected hash."""

    file_path = Path(args.file)

    expected_hash = normalize_hash(args.expected_hash)

    try:

        if not validate_hash(
            expected_hash,
            args.algorithm,
        ):

            expected_length = (
                get_algorithm(args.algorithm)().digest_size * 2
            )

            print(
                "Error: Invalid hash format.",
                file=sys.stderr,
            )

            print(
                f"Expected {expected_length} hexadecimal characters.",
                file=sys.stderr,
            )

            return 1

        print(f"File:      {file_path}")
        print(f"Algorithm: {args.algorithm.upper()}")
        print("Calculating hash...")

        actual_hash, total_bytes = calculate_file_hash_with_progress(
            file_path,
            args.algorithm,
            args.chunk_size,
        )

        print(f"Size:      {format_size(total_bytes)}")
        print(f"Expected:  {expected_hash}")
        print(f"Actual:    {actual_hash}")

        if actual_hash == expected_hash:

            print("\nResult: ✅ HASH MATCHES")
            print("Integrity check passed.")

            return 0

        print("\nResult: ❌ HASH DOES NOT MATCH")
        print("The file may have been modified or corrupted.")

        return 1

    except (
        FileNotFoundError,
        PermissionError,
        ValueError,
    ) as error:

        print(
            f"Error: {error}",
            file=sys.stderr,
        )

        return 1


# ============================================================
# Directory Handling
# ============================================================

def collect_files(
    directory: Path,
    recursive: bool = True,
) -> list[Path]:
    """Collect regular files from a directory."""

    if not directory.exists():
        raise FileNotFoundError(
            f"Directory not found: {directory}"
        )

    if not directory.is_dir():
        raise ValueError(
            f"Not a directory: {directory}"
        )

    if recursive:
        files = [
            path
            for path in directory.rglob("*")
            if path.is_file()
        ]
    else:
        files = [
            path
            for path in directory.iterdir()
            if path.is_file()
        ]

    return sorted(files)


# ============================================================
# Manifest Generation
# ============================================================

def manifest_command(args: argparse.Namespace) -> int:
    """Generate a checksum manifest for a directory."""

    directory = Path(args.directory)
    output_file = Path(args.output)

    try:

        files = collect_files(
            directory,
            recursive=not args.no_recursive,
        )

        if not files:
            print("No files found.")
            return 0

        print(f"Directory: {directory}")
        print(f"Algorithm: {args.algorithm.upper()}")
        print(f"Files:     {len(files)}")
        print()

        manifest_lines = []

        for index, file_path in enumerate(files, start=1):

            relative_path = file_path.relative_to(directory)

            print(
                f"[{index}/{len(files)}] "
                f"Hashing: {relative_path}"
            )

            try:

                digest, total_bytes = calculate_file_hash(
                    file_path,
                    args.algorithm,
                    args.chunk_size,
                )

                manifest_lines.append(
                    f"{args.algorithm.upper()}  "
                    f"{digest}  "
                    f"{relative_path.as_posix()}"
                )

                print(
                    f"    {format_size(total_bytes)} "
                    f"→ {digest}"
                )

            except (
                FileNotFoundError,
                PermissionError,
                ValueError,
            ) as error:

                print(
                    f"    Error: {error}",
                    file=sys.stderr,
                )

                return 1

        try:

            output_file.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            output_file.write_text(
                "\n".join(manifest_lines) + "\n",
                encoding="utf-8",
            )

        except OSError as error:

            print(
                f"Error writing manifest: {error}",
                file=sys.stderr,
            )

            return 1

        print()
        print("✅ Manifest created successfully.")
        print(f"Manifest: {output_file}")
        print(f"Entries:  {len(manifest_lines)}")

        return 0

    except (
        FileNotFoundError,
        PermissionError,
        ValueError,
    ) as error:

        print(
            f"Error: {error}",
            file=sys.stderr,
        )

        return 1


# ============================================================
# Manifest Verification
# ============================================================

def parse_manifest_line(
    line: str,
) -> tuple[str, str, str] | None:
    """
    Parse a manifest line.

    Expected format:

    ALGORITHM  HASH  relative/path
    """

    line = line.strip()

    if not line:
        return None

    if line.startswith("#"):
        return None

    parts = line.split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError(
            f"Invalid manifest line: {line}"
        )

    algorithm = parts[0].lower()
    expected_hash = parts[1].lower()
    relative_path = parts[2]

    if algorithm not in SUPPORTED_ALGORITHMS:
        raise ValueError(
            f"Unsupported algorithm in manifest: {algorithm}"
        )

    return (
        algorithm,
        expected_hash,
        relative_path,
    )


def check_manifest_command(args: argparse.Namespace) -> int:
    """Verify every file listed in a checksum manifest."""

    manifest_path = Path(args.manifest)

    if not manifest_path.exists():
        print(
            f"Error: Manifest not found: {manifest_path}",
            file=sys.stderr,
        )

        return 1

    if not manifest_path.is_file():
        print(
            f"Error: Not a file: {manifest_path}",
            file=sys.stderr,
        )

        return 1

    base_directory = (
        Path(args.directory)
        if args.directory
        else manifest_path.parent
    )

    try:

        lines = manifest_path.read_text(
            encoding="utf-8"
        ).splitlines()

    except (
        OSError,
        UnicodeDecodeError,
    ) as error:

        print(
            f"Error reading manifest: {error}",
            file=sys.stderr,
        )

        return 1

    entries = []

    for line_number, line in enumerate(
        lines,
        start=1,
    ):

        try:

            parsed = parse_manifest_line(line)

            if parsed is not None:
                entries.append(parsed)

        except ValueError as error:

            print(
                f"Error on manifest line "
                f"{line_number}: {error}",
                file=sys.stderr,
            )

            return 1

    if not entries:
        print("Manifest contains no entries.")
        return 0

    print(f"Manifest:  {manifest_path}")
    print(f"Directory: {base_directory}")
    print(f"Files:     {len(entries)}")
    print()

    passed = 0
    failed = 0
    missing = 0

    for index, (
        algorithm,
        expected_hash,
        relative_path,
    ) in enumerate(entries, start=1):

        file_path = base_directory / relative_path

        print(
            f"[{index}/{len(entries)}] "
            f"{relative_path}"
        )

        if not file_path.exists():

            print("    ❌ MISSING")

            missing += 1
            continue

        if not file_path.is_file():

            print("    ❌ NOT A FILE")

            failed += 1
            continue

        try:

            actual_hash, _ = calculate_file_hash(
                file_path,
                algorithm,
                args.chunk_size,
            )

            if actual_hash == expected_hash:

                print(
                    f"    ✅ PASS "
                    f"({algorithm.upper()})"
                )

                passed += 1

            else:

                print(
                    f"    ❌ FAIL "
                    f"({algorithm.upper()})"
                )

                print(
                    f"    Expected: {expected_hash}"
                )

                print(
                    f"    Actual:   {actual_hash}"
                )

                failed += 1

        except (
            FileNotFoundError,
            PermissionError,
            ValueError,
        ) as error:

            print(f"    ❌ ERROR: {error}")

            failed += 1

    print()
    print("=" * 50)
    print("Manifest Verification Summary")
    print("=" * 50)

    print(f"Total:   {len(entries)}")
    print(f"Passed:  {passed}")
    print(f"Failed:  {failed}")
    print(f"Missing: {missing}")

    if failed == 0 and missing == 0:

        print("\n✅ ALL FILES PASSED INTEGRITY CHECK.")

        return 0

    print("\n❌ INTEGRITY CHECK FAILED.")

    return 1


# ============================================================
# Argument Parser
# ============================================================

def create_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""

    parser = argparse.ArgumentParser(
        description=(
            "Advanced file hashing and integrity "
            "verification utility."
        ),
        epilog=(
            "Examples:\n"
            "  python hashing_utility.py hash file.txt\n"
            "  python hashing_utility.py hash file.txt "
            "--algorithm sha512\n"
            "  python hashing_utility.py verify file.txt "
            "<expected_hash>\n"
            "  python hashing_utility.py manifest ./folder\n"
            "  python hashing_utility.py check-manifest "
            "checksums.sha256"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    # --------------------------------------------------------
    # Hash Command
    # --------------------------------------------------------

    hash_parser = subparsers.add_parser(
        "hash",
        help="Generate hashes for one or more files.",
    )

    hash_parser.add_argument(
        "files",
        nargs="+",
        help="Files to hash.",
    )

    hash_parser.add_argument(
        "-a",
        "--algorithm",
        choices=SUPPORTED_ALGORITHMS.keys(),
        default=DEFAULT_ALGORITHM,
        help=(
            "Hash algorithm "
            "(default: sha256)."
        ),
    )

    hash_parser.add_argument(
        "-c",
        "--chunk-size",
        type=int,
        default=DEFAULT_CHUNK_SIZE,
        help=(
            "Chunk size in bytes "
            "(default: 1048576)."
        ),
    )

    hash_parser.add_argument(
        "-p",
        "--progress",
        action="store_true",
        help="Show hashing progress.",
    )

    hash_parser.set_defaults(
        func=hash_command
    )

    # --------------------------------------------------------
    # Verify Command
    # --------------------------------------------------------

    verify_parser = subparsers.add_parser(
        "verify",
        help="Verify a file against an expected hash.",
    )

    verify_parser.add_argument(
        "file",
        help="File to verify.",
    )

    verify_parser.add_argument(
        "expected_hash",
        help="Expected hexadecimal hash.",
    )

    verify_parser.add_argument(
        "-a",
        "--algorithm",
        choices=SUPPORTED_ALGORITHMS.keys(),
        default=DEFAULT_ALGORITHM,
        help=(
            "Hash algorithm "
            "(default: sha256)."
        ),
    )

    verify_parser.add_argument(
        "-c",
        "--chunk-size",
        type=int,
        default=DEFAULT_CHUNK_SIZE,
        help=(
            "Chunk size in bytes "
            "(default: 1048576)."
        ),
    )

    verify_parser.set_defaults(
        func=verify_command
    )

    # --------------------------------------------------------
    # Manifest Command
    # --------------------------------------------------------

    manifest_parser = subparsers.add_parser(
        "manifest",
        help="Generate a checksum manifest for a directory.",
    )

    manifest_parser.add_argument(
        "directory",
        help="Directory to scan.",
    )

    manifest_parser.add_argument(
        "-o",
        "--output",
        default="checksums.sha256",
        help=(
            "Output manifest file "
            "(default: checksums.sha256)."
        ),
    )

    manifest_parser.add_argument(
        "-a",
        "--algorithm",
        choices=SUPPORTED_ALGORITHMS.keys(),
        default=DEFAULT_ALGORITHM,
        help=(
            "Hash algorithm "
            "(default: sha256)."
        ),
    )

    manifest_parser.add_argument(
        "-c",
        "--chunk-size",
        type=int,
        default=DEFAULT_CHUNK_SIZE,
        help=(
            "Chunk size in bytes "
            "(default: 1048576)."
        ),
    )

    manifest_parser.add_argument(
        "--no-recursive",
        action="store_true",
        help=(
            "Only hash files directly inside "
            "the specified directory."
        ),
    )

    manifest_parser.set_defaults(
        func=manifest_command
    )

    # --------------------------------------------------------
    # Check Manifest Command
    # --------------------------------------------------------

    check_parser = subparsers.add_parser(
        "check-manifest",
        help="Verify files using a checksum manifest.",
    )

    check_parser.add_argument(
        "manifest",
        help="Checksum manifest file.",
    )

    check_parser.add_argument(
        "-d",
        "--directory",
        help=(
            "Base directory containing the files. "
            "Defaults to the manifest directory."
        ),
    )

    check_parser.add_argument(
        "-c",
        "--chunk-size",
        type=int,
        default=DEFAULT_CHUNK_SIZE,
        help=(
            "Chunk size in bytes "
            "(default: 1048576)."
        ),
    )

    check_parser.set_defaults(
        func=check_manifest_command
    )

    return parser


# ============================================================
# Main
# ============================================================

def main() -> int:
    """Program entry point."""

    parser = create_parser()

    args = parser.parse_args()

    try:
        return args.func(args)

    except KeyboardInterrupt:

        print(
            "\n\nOperation cancelled by user."
        )

        return 130

    except PermissionError as error:

        print(
            f"Permission denied: {error}",
            file=sys.stderr,
        )

        return 1

    except OSError as error:

        print(
            f"File system error: {error}",
            file=sys.stderr,
        )

        return 1


if __name__ == "__main__":
    sys.exit(main())

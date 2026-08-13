import secrets
import string


def generate_password(length, use_symbols=True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Make sure the password contains all required character types
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(numbers)
    ]

    if use_symbols:
        password.append(secrets.choice(symbols))

    # Create the character pool
    characters = lowercase + uppercase + numbers

    if use_symbols:
        characters += symbols

    # Fill the remaining characters
    remaining = length - len(password)

    for _ in range(remaining):
        password.append(secrets.choice(characters))

    # Securely shuffle the password
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def check_strength(password):
    score = 0

    if len(password) >= 12:
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score == 3:
        return "Moderate"

    elif score == 4:
        return "Strong"

    else:
        return "Very Strong"


print("=" * 50)
print("          SECURE PASSWORD GENERATOR")
print("=" * 50)

try:
    length = int(input("Enter password length: "))

    if length < 8:
        print("\nPassword length must be at least 8 characters.")

    else:
        symbol_choice = input(
            "Include symbols? (y/n): "
        ).lower()

        use_symbols = symbol_choice == "y"

        minimum_length = 4 if use_symbols else 3

        if length < minimum_length:
            print("\nPassword length is too short.")

        else:
            password = generate_password(
                length,
                use_symbols
            )

            strength = check_strength(password)

            print("\n" + "=" * 50)
            print("Generated Password:")
            print(password)
            print("=" * 50)

            print(f"Password Length : {len(password)}")
            print(f"Password Strength: {strength}")

except ValueError:
    print("\nPlease enter a valid number.")

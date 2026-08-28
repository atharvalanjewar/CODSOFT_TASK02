"""
Password Generator Application
Generates a random password of a user-specified length, optionally
including custom characters provided by the user.

Author: Atharva Lanjewar
"""

import random
import string


def generate_password(length, character_pool):
    """Generate a random password of the given length from the character pool."""
    return "".join(random.choice(character_pool) for _ in range(length))


def main():
    print("===== PASSWORD GENERATOR =====\n")

    length = int(input("Enter the desired length of the password: "))

    custom_chars = input(
        "Enter any custom characters you want to include (or press Enter to skip): "
    )

    # Base pool: letters, digits, and symbols
    base_pool = string.ascii_letters + string.digits + string.punctuation

    # Add the user's custom characters into the pool (duplicates just increase their chance of appearing)
    character_pool = base_pool + custom_chars

    password = generate_password(length, character_pool)

    print(f"\nGenerated Password: {password}")


if __name__ == "__main__":
    main()
    
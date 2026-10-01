"""
Secure Password Generator
"""

import secrets
import string
from typing import Optional


def generate_password(
    length: int = 16,
    include_upper: bool = True,
    include_lower: bool = True,
    include_digits: bool = True,
    include_symbols: bool = True,
) -> str:
    """
    Generate a cryptographically secure random password.
    Uses the secrets module (preferred over random for security).
    """
    if length < 4:
        length = 4
    if length > 128:
        length = 128

    alphabet = ""
    required_chars = []

    if include_lower:
        alphabet += string.ascii_lowercase
        required_chars.append(secrets.choice(string.ascii_lowercase))
    if include_upper:
        alphabet += string.ascii_uppercase
        required_chars.append(secrets.choice(string.ascii_uppercase))
    if include_digits:
        alphabet += string.digits
        required_chars.append(secrets.choice(string.digits))
    if include_symbols:
        # Common safe symbols
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        alphabet += symbols
        required_chars.append(secrets.choice(symbols))

    if not alphabet:
        # Fallback
        alphabet = string.ascii_letters + string.digits
        required_chars = [
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.digits),
        ]

    # Fill the rest of the password
    remaining_length = length - len(required_chars)
    if remaining_length < 0:
        # If too many required, just sample from alphabet
        return "".join(secrets.choice(alphabet) for _ in range(length))

    password_chars = required_chars + [
        secrets.choice(alphabet) for _ in range(remaining_length)
    ]

    # Shuffle to avoid predictable positions of required characters
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

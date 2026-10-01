"""
Entropy Calculator for password randomness.
"""

import math
import re
from typing import Dict, Tuple


def calculate_charset_size(password: str) -> int:
    """
    Estimate the size of the character set used by the password.
    """
    size = 0
    if re.search(r"[a-z]", password):
        size += 26
    if re.search(r"[A-Z]", password):
        size += 26
    if re.search(r"\d", password):
        size += 10
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?`~]", password):
        size += 32  # approximate common symbols
    # Fallback for empty or unknown
    if size == 0 and password:
        size = 95  # printable ASCII
    return size


def calculate_entropy(password: str) -> Dict:
    """
    Calculate Shannon entropy approximation for a password.
    Formula: entropy = length * log2(charset_size)
    """
    if not password:
        return {
            "entropy_bits": 0.0,
            "charset_size": 0,
            "classification": "None",
            "length": 0,
        }

    length = len(password)
    charset_size = calculate_charset_size(password)

    if charset_size <= 1:
        entropy = 0.0
    else:
        entropy = length * math.log2(charset_size)

    # Classification
    if entropy < 40:
        classification = "Weak"
    elif entropy < 60:
        classification = "Moderate"
    elif entropy < 80:
        classification = "Strong"
    else:
        classification = "Excellent"

    return {
        "entropy_bits": round(entropy, 2),
        "charset_size": charset_size,
        "classification": classification,
        "length": length,
    }

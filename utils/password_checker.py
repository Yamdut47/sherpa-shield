"""
Password Strength Analysis and Security Score Engine
"""

import re
from typing import Dict, List, Tuple


def analyze_password(password: str) -> Dict:
    """
    Analyze password for various strength criteria.
    Returns a dictionary with checks and overall strength.
    """
    if not password:
        return {
            "length": 0,
            "has_upper": False,
            "has_lower": False,
            "has_digit": False,
            "has_symbol": False,
            "no_common_patterns": False,
            "strength": "None",
            "score": 0,
            "checks": {}
        }

    length = len(password)
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_symbol = bool(re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?`~]", password))

    # Detect common weak patterns
    common_patterns = [
        r"(.)\1{2,}",           # repeated characters (aaa, 111)
        r"(012|123|234|345|456|567|678|789|890)",  # sequential numbers
        r"(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)",  # sequential letters
        r"(qwerty|asdfgh|zxcvbn|password|admin|welcome|login|letmein|monkey|dragon)",  # common words
    ]
    no_common_patterns = not any(re.search(p, password.lower()) for p in common_patterns)

    # Build checks dict
    checks = {
        "Length ≥ 8": length >= 8,
        "Length ≥ 12": length >= 12,
        "Uppercase Letters": has_upper,
        "Lowercase Letters": has_lower,
        "Numbers": has_digit,
        "Symbols": has_symbol,
        "No Common Patterns": no_common_patterns,
    }

    # Calculate score (out of 100)
    score = 0
    if length >= 8:
        score += 10
    if length >= 12:
        score += 15
    if length >= 16:
        score += 10
    if has_upper:
        score += 15
    if has_lower:
        score += 15
    if has_digit:
        score += 15
    if has_symbol:
        score += 20
    if no_common_patterns:
        score += 10

    # Cap at 100
    score = min(score, 100)

    # Determine strength label
    if score < 30:
        strength = "Weak"
    elif score < 55:
        strength = "Medium"
    elif score < 80:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "no_common_patterns": no_common_patterns,
        "strength": strength,
        "score": score,
        "checks": checks,
    }


def get_recommendations(analysis: Dict) -> List[str]:
    """
    Generate actionable security recommendations based on analysis.
    """
    recs = []
    score = analysis.get("score", 0)
    length = analysis.get("length", 0)

    if score >= 80:
        recs.append("Excellent password — suitable for high-value accounts.")
        recs.append("Consider using a password manager to store it securely.")
        return recs

    if length < 12:
        recs.append("Increase length to at least 12 characters (16+ preferred).")
    if not analysis.get("has_upper"):
        recs.append("Add uppercase letters (A-Z).")
    if not analysis.get("has_lower"):
        recs.append("Add lowercase letters (a-z).")
    if not analysis.get("has_digit"):
        recs.append("Include numbers (0-9).")
    if not analysis.get("has_symbol"):
        recs.append("Add special characters (!@#$%^&* etc.).")
    if not analysis.get("no_common_patterns"):
        recs.append("Avoid dictionary words, sequential patterns, and repeated characters.")
    recs.append("Never reuse passwords across different sites.")
    recs.append("Avoid personal information (names, birthdays, phone numbers).")

    return recs

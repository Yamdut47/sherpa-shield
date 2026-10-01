"""
Crack Time Estimator — estimates time to brute-force a password.
"""

import math
from typing import Dict


# Assumptions for offline brute-force (modern GPU cluster ~ 100 billion guesses/sec for simple hashes)
# We use conservative rates for different scenarios.

GUESSES_PER_SECOND = {
    "online_throttled": 10,           # e.g. website login with rate limiting
    "online_unthrottled": 1_000,      # no rate limit
    "offline_slow_hash": 10_000,      # bcrypt / argon2
    "offline_fast_hash": 100_000_000_000,  # MD5 / SHA1 on GPU cluster (~100 GH/s)
}


def format_time(seconds: float) -> str:
    """Convert seconds into a human-readable time string."""
    if seconds < 1:
        return "Instant"
    if seconds < 60:
        return f"{seconds:.1f} seconds"
    minutes = seconds / 60
    if minutes < 60:
        return f"{minutes:.1f} minutes"
    hours = minutes / 60
    if hours < 24:
        return f"{hours:.1f} hours"
    days = hours / 24
    if days < 30:
        return f"{days:.1f} days"
    months = days / 30.44
    if months < 12:
        return f"{months:.1f} months"
    years = days / 365.25
    if years < 100:
        return f"{years:.1f} years"
    if years < 1_000:
        return f"{years:.0f} years"
    if years < 1_000_000:
        return f"{years / 1_000:.1f} thousand years"
    if years < 1_000_000_000:
        return f"{years / 1_000_000:.1f} million years"
    return f"{years / 1_000_000_000:.1f} billion years"


def estimate_crack_time(password: str, entropy_bits: float) -> Dict:
    """
    Estimate crack times under different attack scenarios.
    Uses 2^(entropy) as keyspace size (average case is half of that).
    """
    if not password or entropy_bits <= 0:
        return {
            "keyspace": 0,
            "scenarios": {},
            "primary": "Instant",
        }

    # Average case: half the keyspace
    keyspace = 2 ** entropy_bits
    half_keyspace = keyspace / 2

    scenarios = {}
    for name, gps in GUESSES_PER_SECOND.items():
        seconds = half_keyspace / gps
        scenarios[name] = {
            "seconds": seconds,
            "readable": format_time(seconds),
            "guesses_per_sec": gps,
        }

    # Primary estimate: offline fast hash (most dramatic / educational)
    primary = scenarios["offline_fast_hash"]["readable"]

    return {
        "keyspace": keyspace,
        "scenarios": scenarios,
        "primary": primary,
    }

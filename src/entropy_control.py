"""
Entropy Control Module
Evaluates key randomness and decides adaptive refresh.
"""

import math
from collections import Counter


def calculate_entropy(bits: list[int]) -> float:
    """
    Compute Shannon entropy of a binary key.
    """
    if not bits:
        return 0.0

    counts = Counter(bits)
    total = len(bits)
    entropy = 0.0

    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)

    return entropy


def entropy_secure(entropy: float, threshold: float = 0.98) -> bool:
    """
    Check entropy stability condition.
    """
    return entropy >= threshold

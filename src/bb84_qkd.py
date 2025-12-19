"""
BB84 Quantum Key Distribution Simulation
Generates quantum-inspired cryptographic keys.
"""

import random


def generate_bb84_key(key_length: int = 256) -> list[int]:
    """
    Simulate BB84 key generation.

    Args:
        key_length (int): Number of qubits exchanged.

    Returns:
        list[int]: Shared secret key bits.
    """
    alice_bits = [random.randint(0, 1) for _ in range(key_length)]
    alice_bases = [random.choice(("Z", "X")) for _ in range(key_length)]
    bob_bases = [random.choice(("Z", "X")) for _ in range(key_length)]

    shared_key = []

    for bit, a_basis, b_basis in zip(alice_bits, alice_bases, bob_bases):
        if a_basis == b_basis:
            shared_key.append(bit)

    return shared_key

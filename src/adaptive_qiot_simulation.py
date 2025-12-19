"""
Adaptive Quantum-IoT Encryption Simulation
Simulates entropy-stable secure communication with adaptive key refresh.
"""

import time
import random
from bb84_qkd import generate_bb84_key
from entropy_control import calculate_entropy, entropy_secure


def run_simulation(nodes=200, iterations=500, entropy_threshold=0.98):
    entropy_log = []
    latency_log = []
    refresh_count = 0

    for step in range(iterations):
        combined_key = []

        for _ in range(nodes):
            combined_key.extend(generate_bb84_key(128))

        entropy = calculate_entropy(combined_key)
        entropy_log.append(entropy)

        if not entropy_secure(entropy, entropy_threshold):
            refresh_count += 1
            combined_key = generate_bb84_key(256)

        latency = random.uniform(18, 24)
        time.sleep(latency / 1000)
        latency_log.append(latency)

        if step % 50 == 0:
            print(
                f"Iteration {step} | Entropy: {entropy:.4f} | Latency: {latency:.2f} ms"
            )

    print("\n--- Simulation Summary ---")
    print("Average entropy:", sum(entropy_log) / len(entropy_log))
    print("Average latency:", sum(latency_log) / len(latency_log))
    print("Key refresh events:", refresh_count)


if __name__ == "__main__":
    run_simulation()

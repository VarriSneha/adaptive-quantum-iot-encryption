"""
Adaptive Quantum-IoT Encryption Simulation

Simulates entropy-stable secure communication across
multiple IoT nodes with adaptive key refresh.
"""

import time
import random
from bb84_qkd import generate_bb84_key
from entropy_control import calculate_entropy, entropy_secure


def run_simulation(
    nodes: int = 200,
    iterations: int = 500,
    entropy_threshold: float = 0.98
):
    entropy_log = []
    latency_log = []
    refresh_count = 0

    for step in range(iterations):
        # Simulate multi-node communication
        combined_key = []
        for _ in range(nodes):
            combined_key.extend(generate_bb84_key(128))

        entropy = calculate_entropy(combined_key)
        entropy_log.append(entropy)

        # Adaptive entropy-based key refresh
        if not entropy_secure(entropy, entropy_threshold):
            refresh_count += 1
            combined_key = generate_bb84_key(256)

        # Simulated latency (ms)
        simulated_latency = random.uniform(18, 24)
        time.sleep(simulated_latency / 1000)
        latency_log.append(simulated_latency)

        if step % 50 == 0:
            print(
                f"Iteration {step:3d} | "
                f"Entropy: {entropy:.4f} | "
                f"Latency: {simulated_latency:.2f} ms"
            )

    print("\n--- Simulation Summary ---")
    print(f"Average Entropy    : {sum(entropy_log)/len(entropy_log):.4f}")
    print(f"Average Latency    : {sum(latency_log)/len(latency_log):.2f} ms")
    print(f"Key Refresh Events : {refresh_count}")

    return entropy_log, latency_log


if __name__ == "__main__":
    run_simulation()

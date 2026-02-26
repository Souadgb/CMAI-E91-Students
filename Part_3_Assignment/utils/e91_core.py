"""
E91 Core Functions — Solved implementations from Part 2.

This module provides the complete, solved E91 protocol helper functions
so that Part 3 (Assignment) can use them directly.

These functions build on top of the CHSH core functions (chsh_core.py).
"""

import random
from qiskit import QuantumCircuit
from utils.chsh_core import (
    run_circuit,
    measure_bell_pair,
    create_eavesdropped_state,
    organize_measurements_by_basis,
    calculate_correlations,
    calculate_chsh_value,
    BELL_INEQUALITY_THRESHOLD,
)

# ── E91 Protocol Constants ───────────────────────────────────────────────────
ALICE_BASES = ['0', '45', '90']       # Alice's available bases
BOB_BASES = ['45', '90', '135']       # Bob's available bases
ALICE_CHSH_BASES = ['0', '90']
BOB_CHSH_BASES = ['45', '135']
CHSH_BASIS_PAIRS = [(a, b) for a in ALICE_CHSH_BASES for b in BOB_CHSH_BASES]

EVE_PERCENTAGE_COMPROMISED = 0.7  # Eve intercepts 70% of the pairs


# ── E91 Helper Functions ─────────────────────────────────────────────────────

def generate_random_bases(length: int, options: list) -> list:
    """Generate a list of random measurement bases."""
    return [random.choice(options) for _ in range(length)]


def measure_all_pairs(bell_pairs: list, alice_bases: list, bob_bases: list) -> list:
    """
    Measure each Bell pair with the corresponding bases.

    Returns:
        List of measurement results ('00', '01', '10', '11')
    """
    results = []
    for qc, a_base, b_base in zip(bell_pairs, alice_bases, bob_bases):
        result = measure_bell_pair(qc, a_base, b_base)
        results.append(result)
    return results


def extract_e91_key_and_bell_test_data(results, alice_bases, bob_bases):
    """
    Sift measurement results into key generation and Bell test data.

    Rules:
    - Same basis (45,45) or (90,90) → Key generation
    - CHSH basis pairs → Bell test
    - Other combinations → Discard
    """
    key_results = []
    chsh_results = []
    chsh_alice_bases = []
    chsh_bob_bases = []

    for result, a_base, b_base in zip(results, alice_bases, bob_bases):
        if a_base == b_base:
            key_results.append(result)
        elif (a_base, b_base) in CHSH_BASIS_PAIRS:
            chsh_results.append(result)
            chsh_alice_bases.append(a_base)
            chsh_bob_bases.append(b_base)

    return {
        'key_results': key_results,
        'chsh_results': chsh_results,
        'chsh_alice_bases': chsh_alice_bases,
        'chsh_bob_bases': chsh_bob_bases,
    }

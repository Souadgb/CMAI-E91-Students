"""
CHSH Core Functions — Solved implementations from Part 1.

This module provides the complete, solved CHSH/Bell inequality functions
so that Part 2 (E91 Protocol) can use them directly without importing
from the Part 1 notebook.
"""

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# ── Simulator setup ──────────────────────────────────────────────────────────
GLOBAL_SEED = 91
aer_simulator = AerSimulator()
MANUAL_SIMULATOR_SEED_COUNTER = GLOBAL_SEED

# ── Default CHSH bases (same as Part 1) ──────────────────────────────────────
ALICE_BELL_BASES = ['0', '90']
BOB_BELL_BASES = ['45', '135']

# Theoretical classical limit is 2.0
# In practice, we use a stricter threshold of 2.5 to account for:
#   - Statistical noise in finite shot experiments
#   - Gate errors and decoherence on real hardware
#   - Results must clearly approach the quantum maximum (2√2 ≈ 2.828)
#
# Interpretation:
#   |S| < 2.0       → Classical regime (no violation)
#   2.0 < |S| < 2.5 → Caution: theoretical violation, but may be due to noise or
#                     insufficient statistics (this boundary is a pedagogical choice,
#                     not a scientifically established threshold)
#   |S| > 2.5       → Robust violation, clearly quantum
BELL_INEQUALITY_THRESHOLD = 2.5


# ── Core functions ───────────────────────────────────────────────────────────

def run_circuit(circ: QuantumCircuit, shots=1) -> dict:
    """Run a quantum circuit on the Aer simulator and return counts."""
    global MANUAL_SIMULATOR_SEED_COUNTER

    current_run_seed = MANUAL_SIMULATOR_SEED_COUNTER
    MANUAL_SIMULATOR_SEED_COUNTER += 1

    circ = transpile(circ, aer_simulator)
    result = aer_simulator.run(circ, shots=shots, seed_simulator=current_run_seed).result()
    return result.get_counts(circ)


def create_bell_pair_singlet_state() -> QuantumCircuit:
    """
    Create the Bell singlet state |Ψ-⟩ = (|01⟩ − |10⟩)/√2
    """
    qc = QuantumCircuit(2)

    # Step 1: Create superposition
    qc.h(0)

    # Step 2: Entangle qubits
    qc.cx(0, 1)

    # Step 3: Transform to |Ψ-⟩
    qc.x(1)
    qc.z(1)

    return qc


def apply_basis_transformation(circuit: QuantumCircuit, qubit_index: int, basis: str) -> QuantumCircuit:
    """Apply the appropriate unitary transformation for a given measurement basis."""
    transformed = circuit.copy()

    if basis == '0':
        pass
    elif basis == '90':
        transformed.h(qubit_index)
    elif basis == '45':
        transformed.ry(-np.pi / 4, qubit_index)
    elif basis == '135':
        transformed.ry(-3 * np.pi / 4, qubit_index)
    else:
        raise ValueError(f"Unknown basis: {basis}")

    return transformed


def measure_bell_pair(circuit: QuantumCircuit, alice_basis: str, bob_basis: str) -> str:
    """
    Measure a Bell pair with the given basis choices.
    Returns a 2-bit string like '00', '01', '10', or '11'.
    """
    meas_qc = circuit.copy()

    # Apply basis transformations
    meas_qc = apply_basis_transformation(meas_qc, 0, alice_basis)
    meas_qc = apply_basis_transformation(meas_qc, 1, bob_basis)

    # Measure
    meas_qc.measure_all()

    # Run and return result
    counts = run_circuit(meas_qc, shots=1)
    return list(counts.keys())[0]


def create_eavesdropped_state(bell_qc: QuantumCircuit) -> QuantumCircuit:
    """
    Simulate Eve's intercept-resend attack.
    Eve measures the Bell pair, destroying entanglement,
    then re-prepares a product state based on her measurement outcome.
    """
    eve_qc = bell_qc.copy()
    eve_qc.measure_all()
    eve_result = run_circuit(eve_qc, shots=1)
    eve_bits = list(eve_result.keys())[0]

    qc = QuantumCircuit(2)
    if eve_bits[0] == '1':
        qc.x(1)
    if eve_bits[1] == '1':
        qc.x(0)

    return qc


def organize_measurements_by_basis(results, alice_bases, bob_bases):
    """Group measurement results by (alice_basis, bob_basis) pair."""
    unique_alice = list(set(alice_bases))
    unique_bob = list(set(bob_bases))

    counts = {}
    for a in unique_alice:
        for b in unique_bob:
            counts[(a, b)] = {'00': 0, '01': 0, '10': 0, '11': 0}

    for i, result in enumerate(results):
        a_base = alice_bases[i]
        b_base = bob_bases[i]
        counts[(a_base, b_base)][result] += 1

    return counts


def calculate_correlations(measurements):
    """Compute E(a,b) correlation value for each basis pair."""
    correlations = {}

    for basis_pair, results in measurements.items():
        total = sum(results.values())

        if total > 0:
            E = (results['00'] + results['11'] - results['01'] - results['10']) / total
            correlations[basis_pair] = E
        else:
            correlations[basis_pair] = 0

    print("Correlations:")
    for basis, corr in correlations.items():
        print(f"  E{basis} = {corr:.4f}")

    return correlations


def calculate_chsh_value(correlations, alice_bases=ALICE_BELL_BASES, bob_bases=BOB_BELL_BASES):
    """Compute the CHSH value S from a correlations dict."""
    a1, a2 = alice_bases
    b1, b2 = bob_bases

    S = correlations[(a1, b1)] - correlations[(a1, b2)] + correlations[(a2, b1)] + correlations[(a2, b2)]

    return abs(S)

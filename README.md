# CMAI-E91: Quantum Cryptography Workshop

**Quantum Key Distribution using the E91 Protocol**

This repository contains materials for teaching the E91 quantum key distribution protocol, including the CHSH Bell inequality test that makes it secure.

**Duration:** 1h30 (slides) + 1h30 (hands-on) + assignment  
**Level:** Beginner

---

## Overview

This workshop introduces **Quantum Key Distribution (QKD)** using the **E91 protocol**, which leverages quantum entanglement for secure communication.

You'll learn:
- How quantum entanglement works
- The CHSH Bell inequality test
- How to detect eavesdroppers using quantum mechanics
- Building a complete QKD system

---

## Repository Structure

```text
CMAI-E91/
├── slides/                    # Presentation slides (1h30 theory) — coming soon
├── Part_1_CHSH/               # Notebook 1: Bell Inequality
├── Part_2_E91/                # Notebook 2: QKD Protocol
├── Part_3_Assignment/         # Take-home assignment (Deadline: 24h)
└── requirements.txt
```

---

## Quick Links (Google Colab)

Launch the workshops directly in Google Colab (no local installation required).  
*Each part opens in its own independent Colab environment for a clean start!*

### Guided Workshops
- **Part 1. CHSH Bell Inequality:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/algolab-quantique/CMAI-E91-Students/blob/main/Part_1_CHSH/01_CHSH_Bell_Inequality.ipynb) | [Français](https://colab.research.google.com/github/algolab-quantique/CMAI-E91-Students/blob/main/Part_1_CHSH/01_CHSH_Bell_Inequality_fr.ipynb)
- **Part 2. E91 Protocol:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/algolab-quantique/CMAI-E91-Students/blob/main/Part_2_E91/02_E91_Protocol.ipynb) | [Français](https://colab.research.google.com/github/algolab-quantique/CMAI-E91-Students/blob/main/Part_2_E91/02_E91_Protocol_fr.ipynb)

### Assignment
- **Part 3. Coding Challenge:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/algolab-quantique/CMAI-E91-Students/blob/main/Part_3_Assignment/E91_Assignment_coding.ipynb) | [Français](https://colab.research.google.com/github/algolab-quantique/CMAI-E91-Students/blob/main/Part_3_Assignment/E91_Assignment_coding_fr.ipynb)

---

## Workshop Content

Complete the parts **in order**:

### Part 1: CHSH Bell Inequality (~45 min)
**Learn the fundamentals of quantum entanglement**
- Create Bell pairs (entangled qubit pairs)
- Understand measurement bases
- Implement the CHSH Bell inequality test
- Verify quantum correlations exceed classical limits

### Part 2: E91 Protocol (~45 min)
**Build a complete quantum key distribution system**
- Use your functions from Part 1 (automatically imported!)
- Implement the E91 protocol
- Generate a shared secret key
- Detect eavesdropping attempts
- Decrypt secret messages

### Part 3: Assignment (24h, ~30 min active coding)
**Adapt E91 to a different Bell state**
- Implement E91 using |Φ-⟩ = (|00⟩ - |11⟩)/√2 instead of |Ψ-⟩
- Tasks: create |Φ-⟩ circuit, find the correct CHSH formula
- Theory questions (provided separately)

---

## Key Concepts

| Concept | Classical | Quantum (E91) |
|---------|-----------|---------------|
| Key generation | Computational algorithms | Entangled photons |
| Security basis | Mathematical difficulty | Laws of physics |
| Eavesdrop detection | None inherent | CHSH violation changes |
| CHSH value | \|S\| ≤ 2 | \|S\| ≈ 2.83 |

---

## Prerequisites

- Python 3.9+
- The specific package versions defined in `requirements.txt` are required for reproducibility.

```bash
pip install -r requirements.txt
```

---

## Tips

1. **Run cells in order** — Later cells depend on earlier ones
2. **Read the markdown** — Explanations help you understand the physics
3. **Check your answers** — Each exercise has a test cell
4. **Ask questions** — Quantum mechanics is tricky!

---

## References

- [E91 Original Paper (Ekert, 1991)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.67.661)
- [CHSH Inequality - Wikipedia](https://en.wikipedia.org/wiki/CHSH_inequality)
- [Bell's Theorem - Wikipedia](https://en.wikipedia.org/wiki/Bell%27s_theorem)
- [Qiskit Documentation](https://qiskit.org/documentation/)

---

## Authors
Ibrahim Chegrane

---
# E91 Quantum Key Distribution Workshop

**Duration:** 1h30 (slides) + 1h30 (hands-on)  
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

## Notebooks

Complete the notebooks **in order**:

### 1. [01_CHSH_Bell_Inequality.ipynb](01_CHSH_Bell_Inequality.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/algolab-quantique/CMAI-E91-Students/blob/main/workshops/01_CHSH_Bell_Inequality.ipynb) | [Français](https://colab.research.google.com/github/algolab-quantique/CMAI-E91-Students/blob/main/workshops/01_CHSH_Bell_Inequality_fr.ipynb)
**Learn the fundamentals of quantum entanglement**

- Create Bell pairs (entangled qubit pairs)
- Understand measurement bases
- Implement the CHSH Bell inequality test
- Verify quantum correlations exceed classical limits

~45 minutes

### 2. [02_E91_Protocol.ipynb](02_E91_Protocol.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/algolab-quantique/CMAI-E91-Students/blob/main/workshops/02_E91_Protocol.ipynb) | [Français](https://colab.research.google.com/github/algolab-quantique/CMAI-E91-Students/blob/main/workshops/02_E91_Protocol_fr.ipynb)
**Build a complete quantum key distribution system**

- Use your functions from Notebook 1 (automatically imported!)
- Implement the E91 protocol
- Generate a shared secret key
- Detect eavesdropping attempts
- Decrypt secret messages

~45 minutes

---

## Requirements

We use specific versions of these libraries to guarantee the encrypted messages can be correctly decrypted by your random number generators.

```bash
pip install -r ../requirements.txt
```

---

## Files

```
workshops/
├── 01_CHSH_Bell_Inequality.ipynb    ← Start here!
├── 02_E91_Protocol.ipynb            ← Continue here
├── encrypted_messages.txt           ← Messages to decrypt
└── utils/
    └── encryption_algorithms.py     ← Encryption helpers
```

---

## Tips

1. **Run cells in order** - Later cells depend on earlier ones
2. **Read the markdown** - Explanations help you understand the physics
3. **Check your answers** - Each exercise has a test cell
4. **Ask questions** - Quantum mechanics is tricky!

---

## Key Concepts

| Concept | Classical | Quantum (E91) |
|---------|-----------|---------------|
| Key generation | Computational algorithms | Entangled photons |
| Security basis | Mathematical difficulty | Laws of physics |
| Eavesdrop detection | None inherent | CHSH violation changes |
| CHSH value | |S| ≤ 2 | |S| ≈ 2.83 |

---

## After the Workshop

Complete the [assignment](../assignment/) to test your understanding!


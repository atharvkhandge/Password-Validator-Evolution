# 🛡️ Version 3.0: Heuristic Analysis & zxcvbn

The goal of this version was to reach professional-grade validation by combining traditional complexity rules with modern **entropy-based security analysis**.

### Key Features
* **zxcvbn Integration:** Implemented the `zxcvbn` library to simulate real-world dictionary attacks and pattern recognition.
* **Hybrid Scoring System:** Introduced a weighted calculation that merges **Regex validation (50%)** with **Heuristic strength (50%)** for a final percentage.
* **Actionable Intelligence:** Added automated feedback that provides specific warnings and estimates the time required for offline cracking.

### Learned Concepts
I mastered the distinction between **complexity** (character variety) and **entropy** (unpredictability), learning how to integrate third-party libraries to provide sophisticated, human-readable security audits.

### 🛠️ Dependencies
To run this version, you must install the heuristic engine:
```bash
pip install zxcvbn

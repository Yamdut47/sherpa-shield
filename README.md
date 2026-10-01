# <img width="1254" height="1254" alt="logo" src="https://github.com/user-attachments/assets/72131ea4-2f6f-465a-8756-96dc8bd22b39" />
 SherpaShield



A web-based cybersecurity tool that helps users evaluate and improve password security using password complexity analysis, entropy calculation, attack-resistance estimation, and secure password generation.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Why "SherpaShield"?

**Sherpas** are the legendary mountain guides of the Himalayas — known for unmatched strength, resilience, and protection of those who journey through the world's highest peaks.  

**SherpaShield** carries that same spirit into the digital world: guiding users to stronger passwords and shielding them from cyber threats.

---

## Problem Statement

Many users still rely on weak passwords such as:

- `password123`
- `admin123`
- `qwerty`

These passwords are easily compromised via brute-force, dictionary attacks, and credential stuffing.

**SherpaShield** aims to:

- Analyze password strength
- Calculate entropy
- Estimate crack time
- Provide security recommendations
- Generate strong passwords

---

## Features

| Module | Description |
|--------|-------------|
| **Password Strength Analysis** | Checks length, uppercase, lowercase, numbers, symbols, and common patterns |
| **Security Score Engine** | Generates a score out of 100 |
| **Entropy Calculator** | Measures password randomness in bits |
| **Crack Time Estimator** | Estimates brute-force time under multiple attack scenarios |
| **Password Generator** | Creates cryptographically secure random passwords |
| **Security Recommendations** | Actionable advice based on analysis results |

---

## Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python 3
- **Libraries**: `streamlit`, `re`, `math`, `secrets`, `string`

---

## Project Structure

```
sherpa-shield/
│
├── app.py                  # Main Streamlit application
├── requirements.txt
├── README.md
│
├── assets/
│   ├── logo.png
│   └── screenshots/
│
├── utils/
│   ├── __init__.py
│   ├── password_checker.py # Strength analysis + scoring + recommendations
│   ├── entropy.py          # Entropy calculation
│   ├── crack_time.py       # Crack-time estimation
│   └── generator.py        # Secure password generator
│
└── docs/
    └── project_report.pdf
```

---

## Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/sherpa-shield.git
cd sherpa-shield
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate          # Linux / macOS
# venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## How It Works

```
User
 |
 V
Enter Password
 |
 V
Password Analyzer
 |
 +---- Strength Check
 |
 +---- Entropy Calculation
 |
 +---- Crack Time Estimation
 |
 +---- Recommendations
 |
 V
Results Dashboard
```

### Entropy Formula

```
Entropy (bits) ≈ length × log₂(charset_size)
```

| Entropy Range | Classification |
|---------------|----------------|
| < 40 bits     | Weak           |
| 40–60 bits    | Moderate       |
| 60–80 bits    | Strong         |
| 80+ bits      | Excellent      |

### Security Score (out of 100)

| Criterion              | Points |
|------------------------|--------|
| Length ≥ 8             | +10    |
| Length ≥ 12            | +15    |
| Length ≥ 16            | +10    |
| Uppercase letters      | +15    |
| Lowercase letters      | +15    |
| Numbers                | +15    |
| Symbols                | +20    |
| No common patterns     | +10    |

---

## Target Users

**Primary**
- Students
- General users
- Developers

**Secondary**
- Security researchers
- System administrators
- Organizations

---

## Future Enhancements

| Phase | Feature |
|-------|---------|
| Phase 2 | Have I Been Pwned integration (breach check) |
| Phase 3 | Password history / reuse detection |
| Phase 4 | AI-powered security advisor |

---

## Disclaimer

This tool provides **educational estimates only**. Real-world crack times depend on hashing algorithms, hardware capabilities, and attacker resources. Always use unique, high-entropy passwords stored in a reputable password manager.

---

## License

MIT License — feel free to use and modify for educational or personal projects.

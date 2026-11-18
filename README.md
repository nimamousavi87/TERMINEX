<div align="center">

# 🔴 TERMINEX

### Cross-Platform Diagnostic & Security Toolkit

[🇬🇧 English](README.md) | [🇮🇷 فارسی](README.fa.md)

[![Instagram](https://img.shields.io/badge/Instagram-nima.001n-E4405F?logo=instagram&logoColor=white)](https://instagram.com/nima.001n)
[![Telegram](https://img.shields.io/badge/Telegram-nima__001-26A5E4?logo=telegram&logoColor=white)](https://t.me/nima_001)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Version](https://img.shields.io/badge/Version-1.0.0-red)
![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20Windows%20%7C%20Linux-green)

</div>

---

## ✨ About TERMINEX

TERMINEX is a lightweight, cross-platform Python toolkit designed for network diagnostics, system information, security utilities, and developer tools.

## 🌐 Network Tools

- Local IP Address
- Internet Connection Check
- Ping Tool
- Website Checker
- DNS Lookup
- SSL Certificate Checker

## 💻 System Tools

- System Information
- Storage Information
- Python Information

## 🔐 Security Tools

- Secure Password Generator
- Password Strength Checker

## 🛠 Developer Tools

- Python Version
- Current Date & Time
- Environment Information

---

## 📦 Installation

### Requirements

- Python 3
- Git
- Internet connection for cloning the repository

### Android (Termux)

Update Termux packages:

```bash
pkg update && pkg upgrade -y
```

Install Python and Git:

```bash
pkg install python git -y
```

Clone TERMINEX:

```bash
git clone https://github.com/nimamousavi87/TERMINEX.git
```

Enter the project directory:

```bash
cd TERMINEX
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run TERMINEX:

```bash
python main.py
```

### Windows

1. Install Python 3 and Git.
2. Open Command Prompt or PowerShell.
3. Clone the repository:

```bash
git clone https://github.com/nimamousavi87/TERMINEX.git
```

4. Enter the project directory:

```bash
cd TERMINEX
```

5. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

6. Run the application:

```bash
python main.py
```

### Linux

Install Python 3 and Git using your distribution's package manager.

Then run:

```bash
git clone https://github.com/nimamousavi87/TERMINEX.git
cd TERMINEX
python3 -m pip install -r requirements.txt
python3 main.py
```

---

## 🔄 Updating TERMINEX

To get the latest changes, open a terminal inside the project directory and run:

```bash
git pull origin main
```

Then restart TERMINEX:

```bash
python main.py
```

On Linux, you may need:

```bash
python3 main.py
```

## 📁 Project Structure

```text
TERMINEX/
├── core/
│   ├── __init__.py
│   └── engine.py
├── modules/
│   ├── __init__.py
│   ├── network.py
│   ├── system.py
│   ├── security.py
│   └── developer.py
├── utils/
│   ├── __init__.py
│   ├── colors.py
│   └── helpers.py
├── tests/
├── config.py
├── main.py
├── requirements.txt
├── README.md
└── README.fa.md
```

## 🛠 Troubleshooting

**Python is not recognized**

Make sure Python 3 is installed and available in your system PATH.

**Git is not recognized**

Install Git and restart your terminal.

**Module not found**

Run the dependency installation command from inside the TERMINEX directory.

**Unable to clone the repository**

Check your internet connection and try again.

## 🔐 Responsible Use

TERMINEX is intended for educational purposes, personal use, and authorized diagnostics.

Only examine networks and systems that you own or have explicit permission to test.

## 👨‍💻 Developer

**NIMA**

- Instagram: [@nima.001n](https://instagram.com/nima.001n)
- Telegram: [@nima_001](https://t.me/nima_001)

---

<div align="center">

**TERMINEX v1.0.0**

Built with Python 🔴

</div>

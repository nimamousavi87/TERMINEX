
import secrets
import string
import math


def generate_password():
    print("""
====== ULTRA PASSWORD GENERATOR ======

Choose password length (8 - 128)
""")

    try:
        length = int(input("Length >> "))

        if not 8 <= length <= 128:
            print("Length must be between 8 and 128.")
            return

        chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"

        password = ''.join(
            secrets.choice(chars) for _ in range(length)
        )

        print("\n====== GENERATED PASSWORD ======")
        print(password)
        print("================================")

        entropy = length * math.log2(len(chars))

        print(f"Length: {length}")
        print(f"Estimated Entropy: {entropy:.1f} bits")

    except ValueError:
        print("Invalid input.")


def password_strength():
    password = input("\nEnter password to analyze: ")

    if not password:
        print("Password is empty.")
        return

    score = 0

    checks = {
        "Length >= 12": len(password) >= 12,
        "Lowercase": any(c.islower() for c in password),
        "Uppercase": any(c.isupper() for c in password),
        "Numbers": any(c.isdigit() for c in password),
        "Symbols": any(not c.isalnum() for c in password)
    }

    for label, passed in checks.items():
        print(f"{'[+] ' if passed else '[-] '}{label}")
        score += passed

    levels = {
        0: "Very Weak",
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Strong"
    }

    print("\nPassword Rating:", levels[score])


def security_menu():
    while True:
        print("""
========== SECURITY TOOLS ==========

[1] Ultra Password Generator
[2] Password Strength Checker
[0] Back

====================================
""")

        choice = input("SECURITY >> ").strip()

        if choice == "1":
            generate_password()

        elif choice == "2":
            password_strength()

        elif choice == "0":
            break

        else:
            print("Invalid option.")

        input("\nPress Enter to continue...")

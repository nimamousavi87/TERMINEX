import sys
import os
import platform
import datetime


def python_version():
    print("\nPython Version:", sys.version)


def current_time():
    print("\nCurrent Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def environment_info():
    print("\n====== ENVIRONMENT ======")
    print("Platform:", platform.platform())
    print("Python:", sys.executable)
    print("Working Directory:", os.getcwd())
    print("=========================")


def developer_menu():
    while True:
        print("""
========== DEVELOPER TOOLS ==========

[1] Python Version
[2] Current Date & Time
[3] Environment Information
[0] Back

====================================
""")

        choice = input("DEVELOPER >> ").strip()

        if choice == "1":
            python_version()
        elif choice == "2":
            current_time()
        elif choice == "3":
            environment_info()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

        input("\nPress Enter to continue...")

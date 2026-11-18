import platform
import os
import shutil
import getpass


def system_info():
    print("\n====== SYSTEM INFORMATION ======")
    print("Operating System:", platform.system())
    print("OS Version:", platform.version())
    print("Architecture:", platform.machine())
    print("Python Version:", platform.python_version())
    print("Processor:", platform.processor() or "Unknown")
    print("Username:", getpass.getuser())
    print("Current Directory:", os.getcwd())
    print("================================")


def storage_info():
    print("\n====== STORAGE INFORMATION ======")
    try:
        total, used, free = shutil.disk_usage(os.getcwd())
        print("Total:", round(total / (1024 ** 3), 2), "GB")
        print("Used:", round(used / (1024 ** 3), 2), "GB")
        print("Free:", round(free / (1024 ** 3), 2), "GB")
    except OSError as error:
        print("Storage information unavailable:", error)


def python_info():
    print("\n====== PYTHON INFORMATION ======")
    print("Version:", platform.python_version())
    print("Executable:", os.sys.executable)
    print("================================")


def system_menu():
    while True:
        print("""
========== SYSTEM TOOLS ==========

[1] System Information
[2] Storage Information
[3] Python Information
[0] Back

=================================
""")

        choice = input("SYSTEM >> ").strip()

        if choice == "1":
            system_info()
        elif choice == "2":
            storage_info()
        elif choice == "3":
            python_info()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

        input("\nPress Enter to continue...")

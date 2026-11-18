
from config import APP_NAME, VERSION, BANNER
from utils.colors import Colors
from utils.helpers import clear_screen, pause, print_line

from modules.network import network_menu
from modules.system import system_menu
from modules.security import security_menu
from modules.developer import developer_menu


def red(text):
    return Colors.RED + text + Colors.RESET


def hyperlink(url, label):
    return f"\033]8;;{url}\033\\{label}\033]8;;\033\\"


def show_header():
    print(Colors.TITLE + BANNER + Colors.RESET)

    instagram = hyperlink(
        "https://instagram.com/nima.001n",
        "@nima.001n"
    )

    telegram = hyperlink(
        "https://t.me/nima_001",
        "@nima_001"
    )

    print(f"  {Colors.WHITE}INSTAGRAM : {Colors.RED}{instagram}{Colors.RESET}")
    print(f"  {Colors.WHITE}TELEGRAM  : {Colors.RED}{telegram}{Colors.RESET}")

    print(red("  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"))


def main_menu():
    while True:
        clear_screen()
        show_header()

        print(f"""
{Colors.RED}  [01] {Colors.WHITE}Network Tools
{Colors.RED}  [02] {Colors.WHITE}System Tools
{Colors.RED}  [03] {Colors.WHITE}Security Tools
{Colors.RED}  [04] {Colors.WHITE}Developer Tools
{Colors.RED}  [00] {Colors.WHITE}Exit

{Colors.RED}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

        choice = input(
            f"{Colors.RED}  TERMINEX {Colors.WHITE}>> {Colors.RESET}"
        ).strip()

        if choice in ("1", "01"):
            network_menu()
        elif choice in ("2", "02"):
            system_menu()
        elif choice in ("3", "03"):
            security_menu()
        elif choice in ("4", "04"):
            developer_menu()
        elif choice in ("0", "00"):
            clear_screen()
            print(Colors.RED + "\n  TERMINEX CLOSED SUCCESSFULLY!" + Colors.RESET)
            break
        else:
            print(Colors.ERROR + "\n  INVALID OPTION!" + Colors.RESET)
            pause()


from core.engine import main_menu


def main():
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nTERMINEX stopped.")


if __name__ == "__main__":
    main()

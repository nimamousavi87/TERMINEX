
import socket
import ssl
import time
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import subprocess
import platform


def local_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.connect(("1.1.1.1", 80))
        print("\nLocal IP:", sock.getsockname()[0])
    except OSError:
        print("\nLocal IP: Unavailable")
    finally:
        sock.close()


def internet_check():
    try:
        socket.create_connection(("1.1.1.1", 443), timeout=4)
        print("\n[+] Internet: CONNECTED")
    except OSError:
        print("\n[-] Internet: DISCONNECTED")


def ping_tool():
    host = input("\nEnter IP or domain: ").strip()

    if not host or any(c.isspace() for c in host):
        print("Invalid host.")
        return

    command = ["ping", "-c", "4", host] if platform.system() != "Windows" else ["ping", "-n", "4", host]

    try:
        subprocess.run(command, timeout=15)
    except subprocess.TimeoutExpired:
        print("Ping timed out.")
    except FileNotFoundError:
        print("Ping command is unavailable.")


def dns_lookup():
    domain = input("\nEnter domain: ").strip()

    try:
        addresses = socket.getaddrinfo(domain, None)
        print("\nDNS Results:")

        for ip in sorted({item[4][0] for item in addresses}):
            print(" -", ip)

    except OSError:
        print("DNS lookup failed.")


def website_checker():
    url = input("\nEnter website URL: ").strip()

    if not url:
        print("URL is required.")
        return

    if "://" not in url:
        url = "https://" + url

    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        print("Invalid URL.")
        return

    if parsed.username or parsed.password:
        print("URLs with embedded credentials are not accepted.")
        return

    print("\nChecking website...")

    request = Request(
        url,
        headers={"User-Agent": "TERMINEX/1.0.0"}
    )

    start = time.perf_counter()

    try:
        with urlopen(request, timeout=10) as response:
            elapsed = (time.perf_counter() - start) * 1000

            print("\n====== WEBSITE REPORT ======")
            print("Domain:", parsed.hostname)
            print("HTTP Status:", response.status)
            print("Response Time: %.2f ms" % elapsed)
            print("Final URL:", response.url)
            print("HTTPS:", "Yes" if response.url.startswith("https://") else "No")
            print("============================")

    except HTTPError as error:
        print("Website responded with HTTP status:", error.code)

    except (URLError, OSError, TimeoutError) as error:
        print("Website check failed:", error)


def ssl_checker():
    domain = input("\nEnter domain: ").strip()

    if not domain or "/" in domain or ":" in domain or any(c.isspace() for c in domain):
        print("Enter a valid domain.")
        return

    try:
        context = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as secure:
                cert = secure.getpeercert()

                print("\n====== SSL REPORT ======")
                print("Domain:", domain)
                print("TLS Version:", secure.version())
                print("Certificate Expires:", cert.get("notAfter", "Unknown"))
                print("Certificate Valid: Yes")
                print("=======================")

    except Exception as error:
        print("SSL check failed:", error)


def network_menu():
    while True:
        print("""
========== TERMINEX NETWORK ==========

[1] Local IP Address
[2] Internet Connection
[3] Ping Tool
[4] Website Checker
[5] DNS Lookup
[6] SSL Checker
[0] Back

======================================
""")

        choice = input("NETWORK >> ").strip()

        if choice == "1":
            local_ip()
        elif choice == "2":
            internet_check()
        elif choice == "3":
            ping_tool()
        elif choice == "4":
            website_checker()
        elif choice == "5":
            dns_lookup()
        elif choice == "6":
            ssl_checker()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

        input("\nPress Enter to continue...")

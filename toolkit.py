# toolkit.py
import port_scanner
import brute_forcer
import os

def main():
    print("=== Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. Brute Forcer")
    choice = input("Choose a tool to use (1/2): ").strip()

    if choice == "1":
        target = input("Enter target IP or domain: ").strip()
        start_port = int(input("Enter starting port: ").strip())
        end_port = int(input("Enter ending port: ").strip())

        open_ports = port_scanner.scan_ports(target, start_port, end_port)
        if open_ports:
            print(f"[+] Open ports: {open_ports}")
        else:
            print("[×] No open ports found.")

    elif choice == "2":
        url = input("Enter the login URL: ").strip()
        username = input("Enter the username: ").strip()
        password_file = input("Enter path to password list file: ").strip()

        if not os.path.isfile(password_file):
            print("[!] Password list file not found.")
            return

        with open(password_file, "r", encoding="utf-8", errors="ignore") as f:
            password_list = [pwd.strip() for pwd in f if pwd.strip()]  # skip blanks

        brute_forcer.brute_force_login(url, username, password_list)

    else:
        print("[!] Invalid choice.")

if __name__ == "__main__":
    main()

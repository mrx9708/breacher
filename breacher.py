import requests
import argparse
from colorama import Fore, Style , init
def banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
    ==================================================
    =======|        BREACHER |=======| TOOL |=======| 🔍
    =======|        Python Security Tool 🔐
        ============/============
    =================================================
    =========|
    """)
    print(Fore.YELLOW + "Developed for Learning and testing\n")
def breacher(url):
    admin_paths = [
        "/admin",
        "/admin.php",
        "/wp-admin",
        "/admin1",
        "/admin2",
        "/admin/login",
        "/cPanel",
        "/cpanel",
    ]
    print("starting breacher............")
    for paths in admin_paths:
        full_url = url.strip("/") + paths
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"[+] found url: {full_url}")
            else:
                print(f"[-] failed url: {full_url}")

        except requests.exceptions.RequestException as e:
            print(f"[-] connection error: {full_url},{e}")

parser = argparse.ArgumentParser(description="breacher")
parser.add_argument("-u", "--url", required=True,help="enter url")
args = parser.parse_args()
# run
banner()
breacher(args.url)
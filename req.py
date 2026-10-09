import requests

respon = requests.get("https://www.google.com")
print(respon.status_code)
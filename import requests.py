import requests

req = requests.get("https://www.google.com")
print(req.text)
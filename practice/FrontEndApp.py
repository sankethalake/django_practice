import requests

URL = "http://127.0.0.1:8000/stuinfo/1"

r = requests.get(URL)

print(r.json())


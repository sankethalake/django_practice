import requests
import json
URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name': 'Sanket',
    'roll': '101',
    'city': 'pune'
}
json_data = json.dumps(data)
r = requests.post(URL, json_data)
data = r.json()
print(data)
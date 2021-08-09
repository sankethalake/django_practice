import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


def read(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# read()

def create():
    data = {'name': 'Jay',
            'roll': 104,
            'city': 'mumbai'
            }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


create()


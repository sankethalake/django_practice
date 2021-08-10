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


def create():
    data = {'name': 'rutu',
            'roll': 102,
            'city': 'kolhapur'
            }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


def update():
    data = {'id': 4,
            'name': 'sanket',
            'roll': 104,
            'city': 'pune'
            }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)


def delete_data():
    data = {'id': 5
            }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


# read(1)
create()
# update()
# delete_data()

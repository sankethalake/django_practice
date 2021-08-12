import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


def read(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL,headers={'content-Type': 'application/json'}, data=json_data)
    data = r.json()
    print(data)


def create():
    data = {'name': 'Nitin',
            'roll': 104,
            'city': 'kolhapur'
            }
    headers = {'content'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers={'content-Type': 'application/json'}, data=json_data)
    data = r.json()
    print(data)


def update():
    data = {'id': 4,
            'name': 'sanket',
            'roll': 104,
            'city': 'Pune'
            }
    json_data = json.dumps(data)
    r = requests.put(url=URL, headers={'content-Type': 'application/json'}, data=json_data)
    data = r.json()
    print(data)


def delete_data():
    data = {'id': 4
            }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers={'content-Type': 'application/json'}, data=json_data)
    data = r.json()
    print(data)


# read()
# create()
# update()
delete_data()

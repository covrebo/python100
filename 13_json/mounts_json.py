import json
from pprint import pprint

with open('/Users/chrisovrebo/PycharmProjects/python100/13_json/mount-data.json') as f:
    data = json.load(f)

for item in data['mounts']['collected']:
    pprint(item['name'])
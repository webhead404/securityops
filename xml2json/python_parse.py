import json


with open('attacks.json') as json_file:
    data = json.load(json_file)


for name in data['root']['directive']:
    print ("title: " + name['@name'])
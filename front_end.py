import json

data = json.load(open('example.json'))

start = data['start']

locations = {}
for l in data['locations']:
    locations[l['id']] = l

print(locations)

"""Functions for parsing input"""

import json

def load_file():
    """Load a JSON file and gather game info"""
    data = json.load(open('example.json'))

    # Start location
    start = data['start']

    # Locations
    locations = {}
    connections = {}
    for locn in data['locations']:
        locations[locn['id']] = locn
        connections[locn['id']] = []

    # Events
    events = {}
    for event in data['events']:
        events[event['id']] = event

    # Objects
    objects = {}
    for obj in data['objects']:
        objects[obj['id']] = obj

    # Connections
    # room_id => [(direction, room_id), ...]
    for con in data['connections']:
        connections[con['from']].append((con['direction'], con['to']))
        if con['back'] != 'none':
            connections[con['to']].append((con['back'], con['from']))

    # Bools
    bools = data['bools']

    # Bools
    ints = data['ints']

    # Bools
    strings = data['strings']

    print(connections)

    return (start, locations, events, connections, objects, bools, ints, 
            strings)

if __name__ == "__main__":
    load_file()

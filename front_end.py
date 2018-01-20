"""Functions for parsing input"""

import json

def load_file():
    """Load a JSON file and gather game info"""
    data = json.load(open('example.json'))

    # Start location
    start = data['start']

    # Locations
    locations = {}
    for locn in data['locations']:
        locations[locn['id']] = locn

    # Events
    events = {}
    for event in data['events']:
        events[event['id']] = event

    # Objects
    objects = {}
    for obj in data['objects']:
        objects[obj['id']] = obj

    # Bools
    bools = data['bools']

    # Bools
    ints = data['ints']

    # Bools
    strings = data['strings']

    return (start, locations, events, objects, bools, ints, strings)

if __name__ == "__main__":
    load_file()

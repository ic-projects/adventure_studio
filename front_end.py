"""Functions for parsing input"""

import json

def load_file():
    """Load a JSON file and gather game info"""
    data = json.load(open('example.json'))

    start = data['start']

    locations = {}
    for loc in data['locations']:
        locations[loc['id']] = loc

    print(locations)

if __name__ == "__main__":
    load_file()
    
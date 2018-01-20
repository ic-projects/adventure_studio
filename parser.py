"""Functions for parsing input"""

import location
import tree
import yaml

def parse(program):
    """Load a .adv file and gather game info"""
    data = yaml.load(open(program))

    locations = {}
    for locn_id, locn in data['locations'].items():
        locations[locn_id] = location.Location(locn['name'], locn['description'])
    
    for src, nav in data['navigation'].items():
        for dirn, dest in nav.items():
            locations[src].add_nav(dirn, dest)
    
    start = data['start']

    return tree.Tree(start, locations)

if __name__ == "__main__":
    parse('example.adv')

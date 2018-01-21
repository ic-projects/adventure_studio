"""Functions for parsing input"""

import location, object, tree, utils, yaml

def parse(program):
    """Load a .adv file and gather game info"""
    data = yaml.load(open(program))

    # Parse locations
    locations = {}
    for locn_id, locn in data['locations'].items():
        locations[locn_id] = location.Location(locn['name'], locn['description'])
        try:
            locations[locn_id].add_events(locn['events'])
        except:
            KeyError
        try:
            locations[locn_id].add_objects(locn['objects'])
        except:
            KeyError
    # Parse navigation
    for src, nav in data['navigation'].items():
        for dirn, dest in nav.items():
            locations[src].add_nav(dirn, locations[dest])
    
    # Parse starting location
    start = locations[data['start']]

    return tree.Tree(start, locations)

if __name__ == "__main__":
    parse('example.adv')

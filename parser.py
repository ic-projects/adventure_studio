"""Functions for parsing input"""

import location, object, tree, utils, yaml

def parse(program):
    """Load a .adv file and gather game info"""
    data = yaml.load(open(program))

    # Parse objects
    objects = {}
    for obj_id, obj in data['objects'].items():
        carryable = False
        if carryable in obj:
            carryable = obj[carryable]
        objects[obj_id] = object.Object(obj_id, obj['description'], carryable)

    # Parse locations
    locations = {}
    for locn_id, locn in data['locations'].items():
        locations[locn_id] = location.Location(locn['name'], locn['description'])
        for obj_id in utils.get_list(locn, 'objects'):
            locations[locn_id].add_obj(obj_id, objects[obj_id])
            
    # Parse navigation
    for src, nav in data['navigation'].items():
        for dirn, dest in nav.items():
            locations[src].add_nav(dirn, locations[dest])
    
    # Parse starting location
    start = locations[data['start']]

    return tree.Tree(start, locations)

if __name__ == "__main__":
    parse('example.adv')

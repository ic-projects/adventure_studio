"""Functions for parsing input"""

import location, object, tree, utils, yaml, commands

def parse_cond(cond, locations, event, events, k, loc):
    raise(NotImplementedError)

def parse_command(cmd, locations, event, events, k, loc):
    raise(NotImplementedError)
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
    
    for k, loc in data['locations'].items():
        try:
            events = loc[k]['events']
            for event in events:
                try:
                    conditionals = event['conditional']
                    for conditional in conditionals:
                        locations[k].events[event].add_condition(parse_cond(conditionals[conditional]['if'], locations, event, events, k, loc))
                        for t in conditionals[condition]['then']:
                            locations[k].events[event].append_then(parse_command(t, locations, event, events, k, loc))
                        for t in conditionals[condition]['else']:
                            try:
                                locations[k].events[event].append_else(parse_command(t, locations, event, events, k, loc))
                            except KeyError:
                                pass
                except KeyError:
                    pass
        except KeyError:
            pass
    
    locations["kitchen"].objects["keys"].add_pickup_cmd(commands.AddNavCmd(locations["outside"], locations["hallway"], "north"))
    locations["outside"].events["locked"].add_cond(commands.InCond(locations["outside"].navigation, "north", locations["hallway"])) #commands.InCond(locations["outside"].navigation, "north", "hallway"))
    locations["outside"].events["locked"].append_then(commands.NullCmd())
    locations["outside"].events["locked"].append_else(commands.KillCmd("q"))
    
    # Parse starting location
    start = locations[data['start']]

    return tree.Tree(start, locations)

if __name__ == "__main__":
    parse('example.adv')


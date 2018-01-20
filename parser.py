"""Functions for parsing input"""

import yaml

def parse(program):
    """Load a .adv file and gather game info"""
    data = yaml.load(open(program))

if __name__ == "__main__":
    parse('example.adv')

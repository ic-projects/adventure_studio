import yaml
import sys

if sys.argv[1] == "":
    program = "example.adv"
else:
    program = sys.argv[1]

tree = parse(program)

print(tree['navigation'])

# tree.execute()

def parse(program):
    """ Bitch no comments"""
    return yaml.load(open(program))
    

print("\n\nThanks for playing ;)")

class Tree:
    def __init__(self, start):
        self.start = start
    def execute(self):
        locn = self.start
        while (True):
           locn.enter();


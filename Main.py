import yaml
import sys
import printing

if sys.argv[1] == "":
    program = "example.adv"
else:
    program = sys.argv[1]

tree = parse(program)

tree.execute()
print("\nTHANKS FOR PLAYING!\n")

def parse(program):
    """ Bitch no comments"""
    return yaml.load(open(program))
    

print("\n\nThanks for playing ;)")

class Tree:
    def __init__(self, start):
        self.start = start
    def execute(self):
        locn = self.start
        while locn != None:
            locn.enter()
            locn.doStuff()
            locn = locn.leave()


import sys

if sys.argv[1] == "":
    program = "example.adv"
else
    program = sys.argv[1]

tree = parse(program)

tree.execute()

print("\n\nThanks for playing ;)")

class Tree:
    def __init__(self, start):
        self.start = start
    def execute(self):
        locn = self.start
        while (True):
           locn.enter();


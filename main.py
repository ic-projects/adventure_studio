import parser
import printing
import sys
import tree
import yaml

if len(sys.argv) != 2:
    program = "example.adv"
else:
    program = sys.argv[1]

tree = parser.parse(program)

tree.execute()
print("\nTHANKS FOR PLAYING!\n")


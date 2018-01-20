import parser, printing, sys, tree, yaml

if len(sys.argv) != 2:
    program = "example.adv"
else:
    program = sys.argv[1]

tree = parser.parse(program)

tree.execute()

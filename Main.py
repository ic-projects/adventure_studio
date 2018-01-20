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

class LocationBuilder:
    def __init__(self, type_class, id, description):
        self.type_class = type_class
        self.id = id
        self.description = description
    
    def with_always(self, always):
        self.always = always
    
    def with_choices(self, choices):
        self.choices = choices
    
    def with_objects(self, objects):
        self.objects = objects
    
    def build(self):
        return self.type_class.__class__(self.id, self.description, self.always,
                                         self.choices, self.objects)

class Location:
    def __init__(self, id, description, always, choices, objects):
        self.id          = id 
        self.description = description
        self.always      = always
        self.choices     = choices
        self.objects     = objects

    # Post - after returning from enter we should be able to call self.nextLoc()
    def enter(self):
        raise NotImplementedError

    def nextLoc():
        pass
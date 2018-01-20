class LocationBuilder:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def with_always(self, always):
        self.always = always
    
    def with_choices(self, choices):
        self.choices = choices
    
    def with_objects(self, objects):
        self.objects = objects

    def with_direction(self, direction):
        self.direction = direction
    
    def build(self):
        return Location(self.id, self.description, self.always,
                        self.choices, self.objects, self.direction)

class Direction:
    def __init__(self, n, e, s, w):
        self.north = n
        self.east = e
        self.south = s
        self.west = w

class Location:
    def __init__(self, name, description, always, choices, objects, direction):
        self.name        = name
        self.description = description
        self.always      = always
        self.choices     = choices
        self.objects     = objects
        self.direction = direction

    # Post - after returning from enter we should be able to call self.nextLoc()
    def enter(self):
        raise NotImplementedError

    def nextLoc():
        pass
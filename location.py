class LocationBuilder:
    def __init__(self, idQ, name, description):
        self.id = idQ
        self.name = name
        self.description = description
    
    def with_always(self, always):
        self.always = always
    
    def with_choices(self, choices):
        self.choices = choices
    
    def with_objects(self, objects):
        self.objects = objects
    
    def build(self):
        return Location(self.id, self.description, self.always,
                        self.choices, self.objects)

class Location:
    def __init__(self, idQ, name, description, always, choices, objects):
        self.id          = idQ 
        self.name        = name
        self.description = description
        self.always      = always
        self.choices     = choices
        self.objects     = objects

    # Post - after returning from enter we should be able to call self.nextLoc()
    def enter(self):
        raise NotImplementedError

    def nextLoc():
        pass
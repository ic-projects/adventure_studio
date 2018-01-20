class Events:
    def __init__(id, actions):
        self.id = id
        self.actions = actions

class LocationBuilder:
    def __init__(self, id, description):
        self.id = id
        self.description = description
    
    def with_always(self, always):
        self.always = always
    
    def with_choices(self, choices):
        self.choices = choices
    
    def with_objects(self, objects):
        self.objects = objects
    
    def build(self):
        return Location(self.id, self.description, self.always, self.choices, self.objects)

class Location:
    def __init__(self, id, description, always, choices, objects):
        self.id          = id 
        self.description = description
        self.always      = always
        self.choices     = choices
        self.objects     = objects

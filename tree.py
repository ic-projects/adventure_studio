class Tree:
    def __init__(self, start, locations):
        self.start = start
        self.locations = locations
    def execute(self):
        locn = self.start
        while locn != None:
            locn = locn.enter()

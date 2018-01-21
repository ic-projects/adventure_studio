class Command:
    def execute(self):
        raise NotImplementedError

class sayCmd(Command):
    def __init__(self, str):
        self.str = str

    def execute(self):
       print() 

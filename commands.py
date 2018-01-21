import printing

class Command:
    def execute(self):
        raise NotImplementedError

class Condition:
    def eval(self):
        raise NotImplementedError

class TrueCond(Condition):
    def eval(self):
        return True

class InCond(Condition):
    def __init__(self, dic, key):
        self.dic = dic
        self.key = key
    def eval(self):
        try:
            self.dic[self.key]
            return True
        except KeyError:
            return False

class SayCmd(Command):
    def __init__(self, str):
        self.str = str

    def execute(self):
        exit(1)

class NullCmd(Command):
    def __init__(self):
        pass

class AddNavCmd(Command):
    def __init__(self, origin, dest, direction):
        self.origin = origin
        self.dest = dest
        self.direction = direction
    def execute(self):
        self.origin.add_nav(self.direction, self.dest)
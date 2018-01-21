import printing

class Command:
    def execute(self):
        raise NotImplementedError

class Condition:
    pass

class TrueCond(Condition):
    def eval(self):
        return True

class InCond(Condition):
    def __init__(self, dic, key, val):
        self.dic = dic
        self.key = key
        self.val = val
    def eval(self):
        try:
            if self.dic[self.key] == self.val:
                return True
        except KeyError:
            return False


class KillCmd(Command):
    def __init__(self, str):
        self.str = str

    def execute(self):
        print("Oh no! You've locked yourself out!")
        exit(1)

class NullCmd(Command):
    def __init__(self):
        pass
    def execute(self):
        pass

class AddNavCmd(Command):
    def __init__(self, origin, dest, direction):
        self.origin = origin
        self.dest = dest
        self.direction = direction
    def execute(self):
        self.origin.add_nav(self.direction, self.dest)
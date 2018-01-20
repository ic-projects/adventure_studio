import printing

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.objects = {}
        self.navigation = {}

    def add_nav(self, dirn, dest):
        self.navigation[dirn] = dest

    def add_obj(self, obj_id, obj):
        self.objects[obj_id] = obj

    def enter(self):
        next_locn = self
        
        printing.print_at_speed(self.description,120)
        for dirn, dest in self.navigation.items():
            printing.print_at_speed("To the " + dirn + " there is " + dest.name + ".", 120)

        while(next_locn == self):
            user_input = input()
            command = ""
            operand = ""

            for keyword in ['go', 'pickup']:
                if user_input.startswith(keyword):
                    command = keyword
                    operand = user_input[len(keyword)+1:]

            if (command == 'go'):
                try:
                    next_locn = self.navigation[operand]
                except KeyError:
                    printing.print_at_speed("You can't " + command + " " + operand + "!", 120)

            elif (command == 'pickup'):
                try:
                    self.objects[operand].pickup()
                except KeyError:
                    printing.print_at_speed("You can't " + command + " " + operand + "!", 120)

        return next_locn
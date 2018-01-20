class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.navigation = {}

    def add_nav(self, dirn, dest):
        self.navigation[dirn] = dest

    def enter(self):
        next_locn = self

        print(self.description)

        user_input = input()
        command = ""
        operand = ""
        for keyword in ['go']:
            if user_input.startswith(keyword):
                command = keyword
                operand = user_input[len(keyword)+1:]
        if (command == 'go'):
            try:
                next_locn = self.navigation[operand]
            except KeyError:
                print("You can't go", operand)

        return 
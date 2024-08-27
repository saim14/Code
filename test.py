class Test():
    def __init__(self, integers = 0, floats = 0.0, strings = 'Strings', booleans = True):
        self.integers = int(integers)
        self.floats = float(floats)
        self.strings = str(strings) 
        self.booleans = bool(booleans)

    def get_values(self):
        return self.integers, self.floats, self.strings, self.booleans

    def print_values(self):
        print(f"""Integer: {self.integers}
Floats: {self.floats}
Strings: {self.strings}
Booleans: {self.booleans}""")
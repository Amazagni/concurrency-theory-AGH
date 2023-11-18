class Vertex:
    def __init__(self, letter, number):
        self.letter = letter
        self.number = number

    def __repr__(self):
        if self.number == 0:
            return f"{self.letter}"
        return f"{self.letter}{self.number}"

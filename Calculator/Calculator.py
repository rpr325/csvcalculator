

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = int(a)+int(b)
        return self.result

    def multiply(self, a, b):
        self.result = int(a)*int(b)
        return self.result

    def subtract(self, a, b):
        self.result = int(a)-int(b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = squarerooting(a)
        return self.result
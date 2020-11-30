from CsvReader import CsvReader


def addition(a, b):
    c = a+b
    return c


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = a-b
    return c

def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a*b
    return c

def division(a, b):
    return round((float(a) / float(b)), 9)

def square(a):
    return float(a)**2

def squarerooting(a):
    a = float (a)
    return round((float(a)**.5), 8)

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
from CsvReader import CsvReader


def addition(a, b):
    c = a + b
    return c


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = a - b
    return c

def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c

def division(a, b):
    a = int(a)
    b = int(b)
    c = a / b
    return c

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
        self.result = int(a)/int(b)
        return self.result

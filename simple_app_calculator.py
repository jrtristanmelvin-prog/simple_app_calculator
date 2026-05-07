class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        pass

# Child classes
class Addition(Calculator):
    def calculate(self):
        return self.a + self.b


class Subtraction(Calculator):
    def calculate(self):
        return self.a - self.b


class Multiplication(Calculator):
    def calculate(self):
        return self.a * self.b


class Division(Calculator):
    def calculate(self):
        return self.a / self.b
    
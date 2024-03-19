class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.error = "Something gone wrong"

    def add(self):
        return self.first + self.second

    def subtract(self):
        return self.first - self.second

    def multiply(self):
        return self.first * self.second

    def divide(self):
        return self.first / self.second

    def power(self):
        return self.first ** self.second


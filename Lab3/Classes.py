from Functions1 import filter_prime


class StringClass:
    def __init__(self):
        self.a

    def getString(self):
        self.a = input()
    
    def printString(self):
        print(self.a.upper())


class Shape:
    def __init__(self):
        self.area = 0
    
    def area(self):
        print(self.area)


class Square(Shape):
    def __init__(self, length):
        self.length = length
        self.area = length ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length, self.width = length, width
        self.area = length * width


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def show(self):
        print(self.x, self.y)
    
    def move(self, x, y):
        self.x, self.y = x, y
    
    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** (1 / 2)


class Account:
    def __init__(self, owner, balance):
        self.owner, self.balance = owner, balance
    
    def deposit(self, payment):
        self.balance += payment
    
    def withdraw(self, wd):
        if self.balance < wd:
            print("ERROR: request exceeds current balance")
        else:
            self.balance -= wd


Oleg, Egor = Account("Oleg", 1234), Account("Egor", 5678)
Oleg.deposit(12)
Oleg.deposit(21)
Oleg.withdraw(5678)
Egor.withdraw(5678)

#№6
a = [i for i in range(1, 21)]
print(filter_prime(a))
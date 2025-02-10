import math

# Task 1: Define a class with getString and printString methods
class StringManipulator:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

# Task 2: Define Shape and Square classes
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2

# Task 3: Define Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Task 4: Define Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Task 5: Define Bank Account class
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.balance}")

# Task 6: Filter prime numbers using lambda and filter function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Using lambda and filter to filter prime numbers from a list
numbers = [2, 3, 4, 5, 10, 17, 19, 23, 29, 30]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", prime_numbers)

# Example Usage:

# String Manipulator Example
sm = StringManipulator()
# sm.getString()  # Uncomment to input from user
# sm.printString() # Uncomment to print the upper case

# Shape and Square Example
sq = Square(5)
print("Square Area:", sq.area())

# Rectangle Example
rect = Rectangle(4, 6)
print("Rectangle Area:", rect.area())

# Point Example
p1 = Point(1, 2)
p2 = Point(4, 6)
p1.show()
print("Distance:", p1.dist(p2))

# Bank Account Example
acc = Account("John", 500)
acc.deposit(200)
acc.withdraw(100)
acc.withdraw(700)  # Should show insufficient funds

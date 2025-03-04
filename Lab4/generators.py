# Generator to yield squares of numbers up to N
def squares(n):
    for i in range(n + 1):
        yield i ** 2

# Generator to yield even numbers up to N
def evens(n):
    for i in range(0, n + 1, 2):
        yield i

# Get input from console and print even numbers
n = int(input("Enter a number: "))
print(",".join(map(str, evens(n))))

# Generator for numbers divisible by 3 and 4 in range 0 to N
def div_3_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Generator to yield squares from a to b
def squares_range(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Testing squares_range
a, b = 1, 5
for val in squares_range(a, b):
    print(val)

# Generator to yield numbers from n down to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Testing countdown
n = 5
for val in countdown(n):
    print(val)

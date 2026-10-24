# 1 Write a Python program that checks if a number is positive.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")


# 2 Write a Python program that checks if a given string is empty.
s = input("Enter a string: ")
if s == "":
    print("String is empty")


# 3 Determine if a number is positive, negative, or zero using only if statements.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
if num < 0:
    print("Negative")
if num == 0:
    print("Zero")

# 4 Check if a number is a multiple of both 3 and 5.
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Multiple of both 3 and 5")


# 5 Determine if a given number is a perfect square.
num = int(input("Enter a number: "))
sqrt = int(num ** 0.5)

if sqrt * sqrt == num:
    print("Perfect square")
else:
    print("Not a perfect square")


# 6 Check if a number is divisible by both 2 and 3.
num = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")

# 7 Determine if a number is a perfect cube.
num = int(input("Enter a number: "))

for i in range(-1000, 1001):
    if i ** 3 == num:
        print("Perfect cube")
        break

# 8 Check if a given number is a multiple of 4.
num = int(input("Enter a number: "))

if num % 4 == 0:
    print("Multiple of 4")

# 1 Create a program that prompts the user to enter a password. Keep asking until they enter the correct password.
password = ""
while password != "1234":
    password = input("Enter password: ")
print("Correct password")

# 2 Write a program using a while loop to generate the first n terms of the Fibonacci sequence.
num=5
a=0
b=1
i=0
while num>i:
    print(a)
    c=a+b
    a=b
    b=c
    i=i+1


#Build a program that checks if a given number is prime using a while loop.
num = 7
i = 2
while num > i:
    if num % i == 0:
        print("Not prime")
        break
    i = i + 1
else:
    print("Prime")
print("end")

#Create a program that checks if a given word or phrase is a palindrome (reads the same forwards and backwards) using a while loop.
n = "sos"
while len(n) > 0:
    rev = n[::-1]
    if n == rev:
        print("Palindrome")
    else:
        print("Not a palindrome")
    break


#Write a program to generate the first n rows of Pascal's Triangle using while loops.
n = int(input("Enter number of rows: "))
i = 0
while i < n:
    num = 1
    j = 0
    while j <= i:
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
        j = j + 1

    print()
    i = i + 1
#Create a program that converts a given integer into words (e.g., 123 -> "one hundred twenty-three") using a while loop.
num = int(input("Enter a number: "))
ones = ["zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"]
tens = ["", "", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"]
if num == 0:
    print("zero")
else:
    result = ""
    if num >= 100:
        result = ones[num // 100] + " hundred "
        num = num % 100
    if num >= 20:
        result = result + tens[num // 10] + " "
        num = num % 10
    if num > 0:

        result = result + ones[num]
    print(result)


#Write a program to reverse a given string using a while loop.
s = input("Enter a string: ")
rev = ""
i = len(s) - 1
while i >= 0:
    rev = rev + s[i]
    i = i - 1
print(rev)

#Implement a program to find the greatest common divisor of two numbers using a while loop and the Euclidean algorithm.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b != 0:
    temp = b
    b = a % b
    a = temp
print("GCD:", a)

#Create a program that converts a binary number (entered as a string) to its decimal equivalent using a while loop.
binary = input("Enter binary number: ")
decimal = 0
i = 0
power = 1
while i < len(binary):
    digit = int(binary[len(binary) - 1 - i])
    decimal = decimal + digit * power
    power = power * 2
    i = i + 1
print("Decimal:", decimal)

#Write a program that prints all prime numbers between 1 and 100 using a while loop.
num = 2
while num <= 100:
    i = 2
    while num > i:
        if num % i == 0:
            break
        i = i + 1
    if num == i:
        print(num)
    num = num + 1







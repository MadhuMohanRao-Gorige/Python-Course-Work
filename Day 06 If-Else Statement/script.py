# 1 Check if a given year is a leap year.
year = int(input("Enter year: "))
if year % 400 == 0 and year % 100== 0:
    print("Leap year")
elif year % 4==0 and year % 100!= 0:
    print("Leap year")
else:
    print("Not a leap year")


# 2 Check if a given character is a vowel or consonant.
ch = input("Enter a character: ")
if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")


# 3 Check if a year is a century year (ending in "00").
year = int(input("Enter year: "))
if year % 100 == 0:
    print("Century year")
else:
    print("Not a century year")

# 4 Check if a given number is prime.
num=int(input("Enter a number:"))
for i in range(2,num):
    if num%i==o:
        print("not prime")
        break
    else
        print("Prime")

# 5 Check if a person is eligible to vote based on age.
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 6 Check if a number is positive or non-positive (including zero).
num = int(input("Enter a number: "))
if num==0:
    print("Zero")
elif num > 0:
    print("Positive")
else:
    print("Non-positive")


# 7 Compare two numbers and print the larger one.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(a)
else:
    print(b)

# 8 Check if a character is a letter or not.
ch = input("Enter a character: ")
if ch.isalpha():
    print("Letter")
else:
    print("Not a letter")

# 9 Find and print the smallest of three numbers without using inbuilt methods.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
else:
    print(c)


# 10 Check if a string is a palindrome.
s = input("Enter a string: ")
reverse=s[::-1]
if(s==reverse):
    print("Palindrome")
else:
    print("Not a palindrome")


# 11 Find and print the largest of four numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print(a)
elif b >= a and b >= c and b >= d:
    print(b)
elif c >= a and c >= b and c >= d:
    print(c)
else:
    print(d)

# 12 Take two numbers and determine the sign of their difference.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
diff = a - b
if diff > 0:
    print("Positive")
elif diff < 0:
    print("Negative")
else:
    print("Zero")


# 13 Check if a year is a leap year using an alternative method.
year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")


# 14 Check if a number is a multiple of 7.
num = int(input("Enter a number: "))
if num % 7 == 0:
    print("Multiple of 7")
else:
    print("Not a multiple of 7")


# 15 Calculate and print the absolute value of a number.
num = int(input("Enter a number: "))
if num < 0:
    num = -num
print(num)

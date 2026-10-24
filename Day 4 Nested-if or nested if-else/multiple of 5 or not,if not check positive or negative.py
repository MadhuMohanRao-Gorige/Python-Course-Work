#Question for Nested if-else Statement
#Q2. Write a Python program to check whether a number is a multiple of 5 or not.
# If it is not a multiple of 5, check whether the number is positive or negative and print the result using nested if-else.

num = int(input("Enter a number: "))

if num % 5 == 0:
    print(num, "is a multiple of 5")
else:
    if num > 0:
        print(num, "is not a multiple of 5 and it is positive")
    else:
        print(num, "is not a multiple of 5 and it is negative")
# 1 Write a Python program that converts a temperature in Celsius to Fahrenheit or vice versa based on user input.
choice = input("Enter C for Celsius or F for Fahrenheit: ")
temp = float(input("Enter temperature: "))
if choice == "C":
    f = (temp * 9/5) + 32
    print("Fahrenheit =", f)
elif choice == "F":
    c = (temp - 32) * 5/9
    print("Celsius =", c)
else:
    print("Invalid choice")

#Write a simple calculator program that performs basic arithmetic operations (addition, subtraction, multiplication, division) based on user input.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

#Write a Python program for a simple "Guess the Number" game. Generate a random number, and let the user guess it.
import random
num = random.randint(1,10)
guess = int(input("Guess a number from 1 to 10: "))
if guess == num:
    print("Correct guess!")
else:
    print("Wrong guess!")
    print("Number was", num)

##Write a Python program that checks the strength of a user's password based on certain criteria.
password = input("Enter your password: ")
if len(password) < 8:
    print("Weak password")
elif not any(ch.isupper() for ch in password):
    print("Password must contain an uppercase letter")
elif not any(ch.isdigit() for ch in password):
    print("Password must contain a number")
else:
    print("Strong password")

#Write a Python program that calculates the final price of an item after applying a discount based on the purchase amount.
amount = float(input("Enter purchase amount: "))
if amount >= 5000:
    discount = amount * 20 / 100
elif amount >= 2000:
    discount = amount * 10 / 100
else:
    discount = 0
final_price = amount - discount
print("Discount =", discount)
print("Final price =", final_price)


#Write a Python program that simulates an ATM machine, allowing users to check their balance and withdraw money.
balance = 5000
print("1. Check Balance")
print("2. Withdraw Money")
choice = int(input("Enter choice: "))
if choice == 1:
    print("Balance =", balance)
elif choice == 2:
    amount = int(input("Enter withdrawal amount: "))
    if amount <= balance and amount > 0:
        balance = balance - amount
        print("Remaining balance =", balance)
    else:
        print("Invalid amount or insufficient balance")
else:
    print("Invalid choice")

#Write a Python program that greets the user differently based on the time of day.
hour = int(input("Enter hour (0-23): "))
if hour >= 5 and hour < 12:
    print("Good morning!")
elif hour >= 12 and hour < 17:
    print("Good afternoon!")
elif hour >= 17 and hour < 21:
    print("Good evening!")
elif hour >= 0 and hour < 24:
    print("Good night!")
else:
    print("Invalid hour")

#Write a Python program that calculates the final price of an item after applying a discount coupon code.
price = float(input("Enter item price: "))
coupon = input("Enter coupon code: ")
if coupon == "SAVE10":
    discount = price * 10 / 100
elif coupon == "SAVE20":
    discount = price * 20 / 100
else:
    discount = 0
final_price = price - discount
print("Final price =", final_price)

##Write a Python program that calculates and prints the grade based on a given score, but also validates the input score.
marks = int(input("Enter marks (0-100): "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")

# 10 Write a Python program that acts as a simple calculator and allows the user to choose the operation (addition, subtraction, multiplication, division).
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Choose operation: "))
if choice == 1:
    print("Result =", a + b)
elif choice == 2:
    print("Result =", a - b)
elif choice == 3:
    print("Result =", a * b)
elif choice == 4:
    if b != 0:
        print("Result =", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")





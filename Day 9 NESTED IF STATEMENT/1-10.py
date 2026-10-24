# 1 Given x = 10 and y = 5, write a Python program to determine if x is greater than y. If x is greater than y, check if it's also greater than 15 and print appropriate messages accordingly.
x = 10
y = 5
if x > y:
    print("x is greater than y")
    if x > 15:
        print("x is greater than 15")
    else:
        print("x is not greater than 15")
else:
    print("x is not greater than y")

# 2 Write a Python program that takes a grade as input and prints the corresponding letter grade. If the grade is less than 70, also print "You failed."
grade = int(input("Enter your marks: "))
if grade >= 90:
    print("Grade A")
elif grade >= 80:
    print("Grade B")
elif grade >= 70:
    print("Grade C")
else:
    print("Grade F")
    print("You failed.")

## 3 Write a Python program to check if a person is eligible for a credit card based on their age and income. If the person is underage, print "You are underage." If they are of age but have an income below $30,000, print "Your income is too low for a credit card."
age = int(input("Enter your age: "))
income = int(input("Enter your income: "))
if age < 18:
    print("You are underage.")
else:
    if income < 30000:
        print("Your income is too low for a credit card.")
    else:
        print("You are eligible for a credit card.")

# 4 Write a Python program to determine if a given number num is even or odd. If it's even, check if it's greater than 10 and print appropriate messages.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
    if num > 10:
        print("Number is greater than 10")
    else:
        print("Number is not greater than 10")
else:
    print("Odd number")

# 5 Write a Python program that calculates the ticket price for a theme park based on age and height. If a person is under 12 years old and under 4 feet tall, the ticket price is $10. If they are under 12 but 4 feet tall or taller, the ticket price is $15. If a person is 12 or older and under 4 feet tall, the ticket price is $15. If they are 12 or older and 4 feet tall or taller, the ticket price is $20.
age = int(input("Enter your age: "))
height = float(input("Enter your height in feet: "))
if age < 12:
    if height < 4:
        price = 10
    else:
        price = 15
else:
    if height < 4:
        price = 15
    else:
        price = 20
print("Ticket price: $", price)

''' 6 Write a Python program for user authentication. Ask the user to enter their username and password. 
 If both the username and password are correct, print "Access granted." If the username is 
correct but the password is incorrect, print "Incorrect password." If the username is incorrect, 
print "Invalid username.'''
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin":
    if password == "1234":
        print("Access granted.")
    else:
        print("Incorrect password.")
else:
    print("Invalid username.")

''' 7 Write a Python program for ordering food. Ask the user to select a type of food 
(e.g., "Burger" or "Pizza"). If they choose "Burger," ask if they want fries. If they choose "Pizza," 
ask if they want extra cheese. Print their order with the additional items if chosen.'''
food = input("Choose Burger or Pizza: ")
if food == "Burger":
    fries = input("Do you want fries? yes/no: ")
    if fries == "yes":
        print("Your order: Burger with fries")
    else:
        print("Your order: Burger")
elif food == "Pizza":
    cheese = input("Do you want extra cheese? yes/no: ")
    if cheese == "yes":
        print("Your order: Pizza with extra cheese")
    else:
        print("Your order: Pizza")
else:
    print("Invalid food choice")

''' 8 #Write a Python program that takes an integer as input and checks if it's positive, negative, or zero. 
 If it's positive, check if it's even or odd. Print the appropriate messages.'''
a=int(input("Enter a integer"))
if a>0:
    print("Positive")
    if a%2==0:
        print("Even")
    else:
        print("Odd")
elif a<0:
    print("Negative")
else:
    print("Zero")

''' 9 #Write a Python program that asks for a user's age and checks if they have a driver's license. 
If the user is 18 or older and has a driver's license, print "You are eligible to drive." Otherwise, 
 print "You are not eligible to drive."'''
age=int(input("Enter a person age:"))
license = input("Do you have a driving license? yes/no: ")
if age >=18:
    if licence=="yes":
        print("You are eligible to drive.")
    else:
        print("You are not eligible to drive.")
else:
    print("You are not eligible to drive.")

''' 10 #Write a Python program that checks if a person is eligible to vote. Ask for the person's age and citizenship. 
# If the person is at least 18 years old and a citizen, print "You are eligible to vote." Otherwise, 
# print "You are not eligible to vote."'''

age = int(input("Enter your age: "))
citizen = input("Are you a citizen? yes/no: ")
if age >= 18:
    if citizen == "yes":
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
else:
    print("You are not eligible to vote.")





#Q1. Best Seller Tag Display
#  1 Write a Python program to display "Best Seller" if the product sales are greater than 1000.
sales = int(input("Enter no of sales:"))
if sales > 1000:
    print("Best Seller")


'''2. Instagram Verification Status
Write a Python program to check whether a user gets a verified badge.
check whether the account is eligible for verification and Meta Verified subscription is active.
If active, display "Verified Badge Granted".'''
eligible = input("Is the account eligible? ")
active = input("Is Meta Verified active? ")
if eligible == "yes" and active == "yes":
    print("Verified Badge Granted")

'''Q3. Zepto Rain Delivery Charges
Zepto applies additional delivery charges during rainy weather due to increased delivery
difficulty. Write a Python program that checks whether it is raining and displays "Extra Rain
Charges Applied" if the condition is True. Use an if statement only.'''
rain = input("Enter rain True or False :")
if rain == "True":
    print("Extra Rain Charges Applied")

'''2. if-else Statement Programs
Q1. Username and Password Login
Write a Python program to validate username and password'''
username = input("Username: ")
password = input("Password: ")
if username == "admin" and password == "admin123":
    print("Login Successful")
else:
    print("Invalid Credentials")

#Q2. Product Search
#Write a Python program to check whether a product exists in the available product list.
products = ["Laptop", "Mobile", "Watch"]
search = input("Search Product: ")
if search in products:
    print("Product Found")
else:
    print("Product Not Found")

'''Q3. Delivery Charge Calculation
A food delivery app offers free delivery for orders above ₹99. If the order value is ₹99 or
below, a delivery charge of ₹30 is added to the bill. Write a Python program to calculate and
display the final bill amount using an if-else statement.'''
amount = int(input("Enter the amount :"))
if amount > 99:
    print("Final Bill Amount:", amount)
else:
    amount = amount + 30
    print("Final Bill Amount:", amount)


'''3. if-elif-else Statement Programs
Q1. Weekend Planner Based on Budget
Write a Python program to suggest a weekend plan based on the user's budget.'''
budget = int(input("Enter budget :"))
if budget > 10000:
    print("Plan: Trip")
elif budget > 5000:
    print("Plan: Resort Stay")
elif budget > 3000:
    print("Plan: Movie and Dinner")
elif budget > 1000:
    print("Plan: Cafe and Shopping")
elif budget > 500:
    print("Plan: Street Food and Park Visit")
else:
    print("Plan: Stay Home")

'''Q2. Greeting Based on Time
Write a Python program to display greetings based on the current hour.
Conditions:
● 5 to 11 → Good Morning
● 12 to 16 → Good Afternoon
● 17 to 20 → Good Evening
● Otherwise → Good Night'''
hour = int(input("Enter hour :"))
if hour >= 5 and hour <= 11:
    print("Good Morning")
elif hour >= 12 and hour <= 16:
    print("Good Afternoon")
elif hour >= 17 and hour <= 20:
    print("Good Evening")
else:
    print("Good Night")


'''Q3. Hostinger Hosting Plan
Write a Python program to determine the hosting plan based on the customer's budget.
Conditions:
● Above ₹10000 → Cloud Hosting
● Above ₹5000 → Business Hosting
● Above ₹2000 → Premium Hosting
● Otherwise → Single Hosting'''
budget = int(input("Enter budget :"))
if budget > 10000:
    print("Cloud Hosting")
elif budget > 5000:
    print("Business Hosting")
elif budget > 2000:
    print("Premium Hosting")
else:
    print("Single Hosting")

'''4. Nested if Programs
Q1. Instagram Story Visibility
Write a Python program to check whether a user can view a Close Friends story.
Conditions:
● Check whether the user follows the account.
● If the user follows the account, check whether they are in the Close Friends list.
● If both conditions are True, display "Story Visible".
● Otherwise display the appropriate message.'''
follows = input("Follows Account True or False : ")
friend = input("Close Friend True or False : ")
if follows == "True":
    if friend == "True":
        print("Story Visible")
    else:
        print("Not in Close Friends List")
else:
    print("Follow the Account First")

'''Q2. BGMI Tournament Entry
Write a Python program to check whether a player can join a BGMI tournament.
Conditions:
● Check whether the player has registered.
● If registered, check whether the entry fee is paid.
● If both conditions are True, display "Tournament Entry Confirmed".
● Otherwise display the appropriate message.'''
registered = input("Registered True or False : ")
fee = input("Fee Paid True or False: ")
if registered == "True":
    if fee == "True":
        print("Tournament Entry Confirmed")
    else:
        print("Entry Fee Pending")
else:
    print("Registration Required")

'''Q3. Google Drive File Access
Write a Python program to check whether a user can access a shared file.
Conditions:
● Check whether the file link is active.
● If the link is active, check whether access permission is granted.
● If both conditions are True, display "File Opened Successfully".
● Otherwise display the appropriate message.'''
link = input("Link Active True or False: ")
permission = input("Permission Granted True or False: ")
if link == "True":
    if permission == "True":
        print("File Opened Successfully")
    else:
        print("Access Denied")
else:
    print("Invalid File Link")
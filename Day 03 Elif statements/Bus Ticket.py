#7 Bus Fare:
#Age < 5: "Free"
#Age 5 to 18: "Half Ticket"
#Age > 18: "Full Ticket"
age=int(input("Enter a number:"))
if age<5:
    print("Free")
elif age>=5 and age<=18:
    print("Half Ticket")
else:
    print("Full Ticket")

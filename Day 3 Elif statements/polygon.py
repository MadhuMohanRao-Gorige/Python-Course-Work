#6.Input the number of sides and determine the type of polygon:
#3 → Triangle
#4 → Quadrilateral
#5 → Pentagon
#Else → Unknown shape
sides = int(input("Enter number of sides: "))
if sides == 3:
    print("Triangle")
elif sides == 4:
    print("Quadrilateral")
elif sides == 5:
    print("Pentagon")
else:
    print("Unknown shape")



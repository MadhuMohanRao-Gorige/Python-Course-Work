#1.Write a Python program to check whether a given number is a multiple of 5.
 #If the number is a multiple of 5, then check whether it is also even or odd and print the appropriate message using nested if.
num = int(input("Enter a number: "))
if num % 5 == 0:
    if num % 2 == 0:
        print("Multiple of 5 and Even")
    else:
        print("Multiple of 5 and Odd")
else:
    print("Not a multiple of 5")

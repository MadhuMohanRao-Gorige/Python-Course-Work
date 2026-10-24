#1.Take a character input and check whether it is uppercase letter or lowercase letter or not letter.
ch = input("Enter a character: ")
if ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
else:
    print("Not letter")

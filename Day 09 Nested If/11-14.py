# 11 Write a Python program that takes three numbers as input and prints them in ascending order.
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=int(input("Enter the third number :"))
numbers=[a,b,c]
numbers.sort()
print(numbers)

#for decending order
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=int(input("Enter the third number :"))
numbers=[a,b,c]
numbers.sort(reverse=True)
print(numbers)

''' 12 #Write a Python program for a store that calculates discounts based on the purchase amount and membership status. 
# Ask the user for the purchase amount and whether they have a membership. If the purchase amount is greater 
# than $100 and they have a membership, apply a 20% discount. If the purchase amount is greater than $100 without 
# membership, apply a 10% discount. Otherwise, no discount is applied.'''
amount = int(input("Enter purchase amount: "))
membership = input("Enter membership True or False: ")
if amount > 100:
    if membership == "True":
        amount = amount - (amount * 20 / 100)
        print("Final amount:", amount)
    else:
        amount = amount - (amount * 10 / 100)
        print("Final amount:", amount)
else:
    print("Final amount:", amount)

''' 13 #Write a Python program that classifies a character as a vowel, consonant, or neither. Ask the user to enter 
# a single character. If it's a vowel (a, e, i, o, u), print "Vowel." If it's a consonant, print "Consonant." 
# If it's neither (e.g., a digit or special character), print "Neither."'''
ch = input("Enter a character: ")
if ch in "aeiouAEIOU":
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Neither")

''' 14 #Write a Python program that recommends books based on the reader's age and genre preference. 
# Ask the user for their age and favorite genre ("Mystery," "Fantasy," or "Science Fiction"). 
# Recommend different books based on their input.'''
age = int(input("Enter your age: "))
genre = input("Enter your favorite genre: ")
if age < 13:
    if genre == "Fantasy":
        print("Recommended Book: Harry Potter")
    elif genre == "Mystery":
        print("Recommended Book: The Boxcar Children")
    elif genre == "Science Fiction":
        print("Recommended Book: A Wrinkle in Time")
    else:
        print("Invalid genre")
else:
    if genre == "Fantasy":
        print("Recommended Book: The Hobbit")
    elif genre == "Mystery":
        print("Recommended Book: Sherlock Holmes")
    elif genre == "Science Fiction":
        print("Recommended Book: Dune")
    else:
        print("Invalid genre")














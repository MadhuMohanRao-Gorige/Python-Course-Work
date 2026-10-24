# 1 Basic Counting: Write a while loop that counts from 1 to 10 and prints each number.
i = 1
while i <= 10:
    print(i)
    i = i + 1

# 2 Create a program that asks the user to enter a number, and then use a while loop to count down from that number to 1, printing each value.
num = int(input("Enter a number: "))
while num >= 1:
    print(num)
    num = num - 1

# 3 Write a while loop that calculates the sum of even numbers from 1 to 100.
i=1
sum=0
while i<=100:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)

""" 4 Create a simple number guessing game using a while loop. Generate a random number and
 have the user guess it, giving hints like "too high" or "too low" until they guess correctly."""
'''import random
num = random.randint(1, 10)
guess = 0
while guess != num:
    guess = int(input("Guess a number from 1 to 10: "))
    if guess > num:
        print("Too high")
    elif guess < num:
        print("Too low")
    else:
        print("Correct!")'''

# 5 Use a while loop to calculate the factorial of a given number.
n=5
fact=1
while n>0:
    fact=fact*n
    n=n-1
print(fact)

# 6 Write a while loop that prints all even numbers between 1 and 50.
i=1
num=50
while i<=50:
    if i%2==0:
        print(i)
    i=i+1
# 7 Create a program that calculates the sum of the digits of a given integer using a while loop.
int=234
sum=0
while int>0:
    i=int%10
    sum=sum+i
    int=int//10
print(sum)

# 8 Generate a multiplication table for a given number using a while loop.
num=5
i=1
while i<=10:
    print(num,"x",i,"=",num*i)
    i=i+1

# 9 Write a program to find all the factors of a given number using a while loop.
num=12
i=1
while num>=i:
    if num%i==0:
        print(i)
        i=i+1

# 10 Implement a program that reverses even numbers using a while loop.
num = int(input("Enter an even number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(rev)








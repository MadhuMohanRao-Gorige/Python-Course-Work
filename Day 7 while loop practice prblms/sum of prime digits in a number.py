# write a program to find the sum of prime digits in a number
num = 123456
total = 0
while num > 0:
    digit = num % 10
    if digit in [2, 3, 5, 7]:
        total = total + digit
    num = num // 10
print("Sum of prime digits:", total)
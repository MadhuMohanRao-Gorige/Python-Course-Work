# 4 write a program to find the sum of alternate digits in a number
num = 123456
sum = 0
count = 0
while num > 0:
    digit = num % 10
    if num % 2 == 0:
        sum = sum + digit
    num = num // 10
    count = count + 1
print("Sum of alternate digits:", sum)
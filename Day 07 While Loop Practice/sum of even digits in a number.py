#1 n=1,2,3,4,5,6 write a program to find the sum of even digits in a number
num = 123456
sum = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        sum = sum + digit
    num = num // 10
print(sum)
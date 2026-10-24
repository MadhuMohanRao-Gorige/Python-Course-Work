#21 Calculate the power of a number using a for loop ?
num = 2
power = 3
result = 1
for i in range(power):
    result = result * num
print(result)

# 22 Reverse a list using a for loop ?
a = [1, 2, 3, 4, 5]
rev = []
for i in a:
    rev = [i] + rev
print(rev)

# 23 Find and print the largest element in a list using a for loop ?
a = [10, 25, 5, 40, 15]
largest = a[0]
for i in a:
    if i > largest:
        largest = i
print(largest)

# 24 Calculate the average of numbers in a list using a for loop ?
a = [6, 3, 6, 5]
avg = 0
for i in a:
    avg = avg + i
print(avg/ len(a))

# 25 Print a countdown from a given number using a for loop ?
num = 5
for i in range(num, 0, -1):
    print(i)

# 26 Generate a pattern of numbers using nested for loops ?
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 27 Calculate the product of elements in a list using a for loop ?
a = [2, 3, 4]
product = 1
for i in a:
    product = product * i
print(product)

# 28 Find and print the position (index) of an element in a list using a for loop ?
a = [10, 20, 30, 40]
num = 30
for i in range(len(a)):
    if a[i] == num:
        print(i)

# 29 Calculate the sum of all odd numbers from 1 to 100 using a for loop ?
sum = 0
for i in range(1, 101):
    if i % 2 != 0:
        sum = sum + i
print(sum)

# 30 Print a triangle of asterisks using a for loop ?
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()







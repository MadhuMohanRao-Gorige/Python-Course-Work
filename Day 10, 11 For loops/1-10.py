# 1 Print numbers from 1 to 5 using a for loop?
for i in range(1, 6):
    print(i)

# 2 Calculate the sum of numbers from 1 to 10 using a for loop ?
sum = 0
for i in range(1, 11):
    sum = sum + i
print(sum)

# 3 Print even numbers from 1 to 10 using a for loop?
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# 4 Calculate the factorial of a number using a for loop?
n = 5
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)

# 5 Print elements of a list using a for loop ?
a = [10, 20, 30, 40, 50]
for i in a:
    print(i)

# 6 Find the maximum value in a list using a for loop ?
a = [10, 25, 5, 40, 15]
maximum = a[0]
for i in a:
    if i > maximum:
        maximum = i
print(maximum)

# 7 Print characters in a string using a for loop ?
s = "Python"
for i in s:
    print(i)

# 8 Count the number of vowels in a string using a for loop ?
s = "hello world"
count = 0
for i in s:
    if i in "aeiou":
        count = count + 1
print(count)


# 9 Iterate over a dictionary and print key-value pairs using a for loop ?
a = {"name": "Madhu", "age": 22, "city": "Hyderabad"}
for key, value in a.items():
    print(key, value)

# 10 Print a pattern using nested for loops ?
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()



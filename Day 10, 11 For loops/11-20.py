# 11 Calculate the sum of all even numbers from 1 to 100 using a for loop ?
sum=0
for i in range(1,101):
    if i%2==0:
        sum = sum + i
print(sum)

# 12 Print the first 10 Fibonacci numbers using a for loop ?
a = 0
b = 1
for i in range(10):
    print(a)
    c = a + b
    a = b
    b = c

# 13 Find and print the common elements between two lists using a for loop ?
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
for i in a:
    if i in b:
        print(i)

# 14 Generate a multiplication table for a given number using a for loop ?
num=12
for i in range(1,11):
    print(num,"x",i ,"=" ,num*i)

# 15 Calculate the factorial of a number using a for loop with a range starting from 1 ?
n=5
fact=1
for i in range(1, n+1):
    fact =fact * i
print(fact)


# 16 Print the reverse of a string using a for loop ?
s = input("Enter a string: ")
rev = ""
for i in s:
    rev = i + rev
print(rev)

# 17 Generate a list of squares for numbers from 1 to 10 using a for loop ?
for i in range(1, 11):
    print(i * i)

# 18 Count the number of words in a sentence using a for loop ?
s = input("Enter a sentence: ")
count = 0
for i in s.split():
    count = count + 1
print(count)

# 19 Calculate the sum of digits in a number using a for loop ?
num = input("Enter a number: ")
sum = 0
for i in num:
    sum = sum + int(i)
print(sum)

# 20 Generate a list of prime numbers within a given range using a for loop ?
start = int(input("Enter start: "))
end = int(input("Enter end: "))
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)







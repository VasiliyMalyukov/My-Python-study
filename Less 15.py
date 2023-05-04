# Lesson topic 'common scenarios'

counter = 0
for i in range(10):
    num = int(input())
    if num > 10:
        counter = counter + 1
print('Было введено', counter, 'чисел, больших 10.')

print()

counter1 = 0
counter2 = 0
for i in range(10):
    num = int(input())
    if num > 10:
        counter1 = counter1 + 1
    if num == 0:
        counter2 = counter2 + 1
print('Было введено', counter1, 'чисел, больших 10.')
print('Было введено', counter2, 'нулей.' )

print()

counter = 0
for i in range(1, 101):
    if i**2 % 10 == 4:
        counter = counter + 1
print(counter)

print()

total = 0
for i in range(1, 6):
    total += i
    print(total, end=' ')

# Task 1: 'Amount of numbers'. The program takes two integers as input A and B. Write a program
# that counts th number of numbers in the range from A to B inclusive, whose cube
# ends in 4 or 9.

counter = 0
for i in range(int(input()), int(input()) + 1):
    if (i**3 % 10 == 4) or (i**3 % 10 == 9):
        counter = counter + 1
print(counter)

# Task 2: 'Sum of numbers'. The unput to the program is a natural number N and then N integers,
# each on a separate line. Write a program that calculates the sum of the given numbers.

total = 0
for _ in range(int(input())):
    total += int(input())
print(total)

# Task 3: 'Asymptotic approximation'. The input to the program is a natural number N.
# Write a program that evaluates the value of an expression (1 + 1/2 +1/3 + ... + 1/n) - ln(n)

from math import log

n = int(input())

num = 0
for i in range(1, n +1):
    num = num + (1 / i)
    num2 = num - log(n)
print(num2)

# Task 4: 'Sum of numbers 2'. The input to the program is a natural number N. Write a program
# that calculates the sum of those numbers from 1 to N (inclusive)
# whose square ends in 2, 5 or 8.

n = int(input())

counter = 0
for i in range(1, n + 1):
    if (i**2 % 10 == 2) or (i**2 % 10 == 5) or (i**2 % 10 == 8):
        counter = counter + i
print(counter)

# Task 5: 'Factorial'. The input to the program is a natural number N. Write a program
# that calculates n!.

total = 1
for i in range(1, int(input()) + 1):
    total = total * i
print(total)

# Task 6: 'No zeros'. Write a program that reads 10 numbers and prints the product of the
# non-zero numbers.

total = 1
for _ in range(10):
    n = int(input())
    if n > 0:
        total = total * n
print(total)

# Task 7: 'Sum of divisors'. The input to the program is a number N. Write a program that
# calculates the sum of all its divisors.

n = int(input())

total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += i
print(total)

# Task 8: 'Alternating sum'. The input to the program is a natural number N. Write a program
# to calculate rhe alternating sum.

n = int(input())

count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        count -= i
    else:
        count += i
print(count)

# Task 9: 'Biggest numbers'. The input to the program is a natural number N and then N distinct
# natural numbers, each on a separate line. Write a program that prints the largest and second
# largest number in a sequence.

largest = 0
largest1 = 0
for i in range(1, int(input()) + 1):
    n = int(input())
    if largest < n:
        largest1 = largest
        largest = n
    elif largest1 < n:
        largest1 = n
print(largest)
print(largest1)

# Task 10: 'Only even numbers'. Write a program that reads a sequence of 10 integers and
# determines whether each of them is even or not.

counter = 0

for i in range(10):
    n = int(input())
    if n % 2 == 0:
        counter = counter
    elif n % 2 != 0:
        counter = counter + 1

if counter == 0:
    print('YES')
else:
    print('NO')

# Task 11: 'Fibonacci sequence'. Write a program that reads a natural number N and outputs the
# first N numbers of the Fibonacci sequence.

n = int(input())
x = 1
y = 0

for i in range(1, n + 1):
    x, y = y, x + y
    print(y, end=' ')

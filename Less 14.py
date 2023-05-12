# Lesson topic 'for loop'

# Task 1: Given two integers M and N. Write a program that print all numbers from M to N inclusive.

m, n = int(input()), int(input())

for i in range(m, n + 1):
    print(i)

# Task 2: Given two integers M and N. Write a program that all numbers from M to N inclusive in ascending order
#  if M<N, or in descending order otherwise.

m, n = int(input()), int(input())

if m < n:
    for i in range(m, n + 1):
        print(i)
elif m > n:
    for i in range(m, n - 1, - 1):
        print(i)
else:
    print(m)

# Task 3: Given two integers M and N. Write a program that prints all odd numbers from M to N inclusive
# in descending order.

m, n = int(input()), int(input())

for i in range (m, n - 1, - 1):
    if i % 2 == 1:
        print(i)

# Task 4: Given two natural numbers M and N. Write a program that prints all numbers from M to N inclusive
# satisfying at least one of the following conditions:
# the number is a multiple of 17;
# the number ends in 9;
# the number is a multiple of 3 and 5 at the same time.

m, n = int(input()), int(input())

for i in range(m, n + 1):
    if i % 17 == 0:
        print(i)
    elif i % 10 == 9:
        print(i)
    elif (i % 3 == 0) and (i % 5 == 0):
        print(i)

# Task 5: Given a natural number N. Write a program that prints the multiplication table for N.

n = int(input())

for i in range(1, 11):
    print(n, 'x', i, '=', n * i)
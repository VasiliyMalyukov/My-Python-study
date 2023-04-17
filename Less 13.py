# Lesson topic 'loop variable' and 'loop variable names'

for i in range(10):
    print(i, '-- Привет')

print()

for i in range(10):
    print(i + 1, '-- Привет')

print()

for _ in range(5):
    print('Python - awesome!')

print()

# Task 1: 'Repeat after me 2'. Write a program that reads one line of text and outputs 10 lines,
# numbered 0 to 9, each with a specified line of text.

text = input()

for i in range(10):
    print(i, text)

# Task 2: 'Number square'. The input to the program is a natural number N. Write a program that
# for each of the numbers from 0 to N (inclusive) prints the phrase 'The square of the number
# [number] is [number]'.

n = int(input())

for i in range(n + 1):
    print('Квадрат числа', i, 'равен', i * i)

# Task 3: 'Star triangle'. Write a program that prints a star triangle.

n = int(input())

for i in range(n):
    print('*' * (n - i))

# Task 4: 'Population'. The input to the program is three natural numbers M, P, N.
# M - starting number of organism;
# P - average daily increase in %;
# N - number of days to breed.
# Write a program that predicts the size of a population of organism. The program should output
# the population size on each day, starting with 1 and ending n-th day.

m, p, n = float(input()), float(input()), int(input())

for i in range(n):
    print(i + 1, m * ((1 + p / 100) ** i))
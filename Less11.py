# Lesson topic: math module

import math

num1 = math.sqrt(2)     # вычисление корня квадратного из двух
num2 = math.ceil(3.8)   # округление числа вверх
num3 = math.floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)

print()

from math import *

num1 = sqrt(2)     # вычисление корня квадратного из двух
num2 = ceil(3.8)   # округление числа вверх
num3 = floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)


# Task 1: 'Euclidean distance'. Write a program that determines the Euclidean distance between
# two points whose coordinates are given.

from math import *

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

print(sqrt(pow((x1 - x2), 2) + (pow((y1 - y2), 2))))


# Task 2: 'Area and length'. Write a program that determines the area of a circle and the circumference
# of a circle given a given radius.

from math import *

r = float(input())

print(pi * pow(r, 2))
print(2 * pi * r)


# Task 3: 'Averages'. In mathematics, the following averages are distinguished:
# arithmetic mean of numbers, geometric mean of numbers, harmonic mean of numbers,
# mean square of numbers. The input to the program is two real numbers A and B, each on a separate line.
# The program should display 4 numbers - the arithmetic mean, geometric mean, harmonic and quadratic.

from math import *

a, b = float(input()), float(input())

print((a + b) / 2)
print(sqrt(a * b))
print((2 * a * b) / (a + b))
print(sqrt((pow(a, 2) + pow(b, 2)) / 2))


# Task 4: 'Trigonometric expression'. Write a program that calculates the value of
# a trigonometric expression given the number of degrees X.

from math import *

x = float(input())

print(sin(radians(x)) + cos(radians(x)) + (
    pow(tan(radians(x)), 2)))


# Task 5: 'Floor and celling'. Write a program that calculates the values |x| + [x]
# given a real number X.

from math import *

x = float(input())

print(floor(x) + ceil(x))

# Task 6: 'Quadratic equation'

from math import *

a, b, c = float(input()), float(input()), float(input())

discr = b ** 2 - 4 * a * c

if discr > 0:
    x1 = (-b + sqrt(discr)) / (2 * a)
    x2 = (-b - sqrt(discr)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
elif discr == 0:
    print(-b / (2 * a))
else:
    print("Нет корней")


# Task 7: 'Regular polygon'. A regular polygon is a convex polygon in which all sides and all angels
# between adjacent sides are equal. Two numbers are given: a natural number N and a real number A.
# Write a program that finds the area of a given regular polygon.

from math import *

n, a = int(input()), float(input())

print((n * (a ** 2)) / (4 * tan(pi / n)))

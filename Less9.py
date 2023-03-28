# Lesson topic: numeric data types

a = 13
b = 7

total = a + b
diff = a - b
prod = a * b
div1 = a / b
div2 = a // b
mod = a % b
exp = a ** b

print(a, '+', b, '=', total)
print(a, '-', b, '=', diff)
print(a, '*', b, '=', prod)
print(a, '/', b, '=', div1)
print(a, '//', b, '=', div2)
print(a, '%', b, '=', mod)
print(a, '**', b, '=', exp)

print()

atom = 10 ** 80  # количество атомов во вселенной
print('Количество атомов =', atom)

print()

a = 13.5
b = 2.0

total = a + b
diff = a - b
prod = a * b
div = a / b
exp = a ** b

print(a, '+', b, '=', total)
print(a, '-', b, '=', diff)
print(a, '*', b, '=', prod)
print(a, '/', b, '=', div)
print(a, '**', b, '=', exp)

print()

# Task 1: 'Area of a triangle'. Write a program that reads the lengths of two legs in a right triangle
# and prints its area.

a = float(input())
b = float(input())

s = (1 / 2) * a * b
print(s)


# Task 2: 'Two old ladies'. Two old women walk towards each other with constant speeds V1 and V2 km/h. Determine after what time the old women will meet if the distance between them is equal to S km.

s = float(input())
v1 = float(input())
v2 = float(input())

print(s / (v1 + v2))


# Task 3: 'Reciprocal number'. Write a program that reads one number from the keyboard and prints its inverse. If at the same time the number entered from the keyboard is zero, then print 'Reciprocal number does not exist' (without quotes).

x = float(input())

if x == 0:
    print('Обратного числа не существует')
else:
    print(1 / x)


# Task 4: '451 degrees Fahrenheit'. The famous American writer Ray Bradbury has a novel 'Fahrenheit 451'. Write a program that determines what temperature on the Celsius scale corresponds to the specified value on the Fahrenheit scale.

f = float(input())

print((5 / 9) * (f - 32))


# Task 5: 'Dog age'. The input to the program is the number N - the number of dog years. Write a program that calculates the age of a dog in human years.

n = float(input())

if (n == 1) or (n == 2):
    print(n * 10.5)
else:
    print(21 + (n - 2) * 4)


# Task 6: 'First digit after dot'. Given a positive real number. Print its first digit after the decimal point.

x = float(input())
y = int(x * 10)

print(y % 10)


# Task 7: 'Fraction'. Given a positive real number. Print its fractional part.

x = float(input())
y = int(x)

print(x - y)


# Task 8: 'The largest and smallest'. Write a program that finds the smallest and largest of five numbers.

n1, n2, n3, n4, n5 = int(input()), int(input()), int(
    input()), int(input()), int(input())

print('Наименьшее число', '=', min(n1, n2, n3, n4, n5))
print('Наибольшее число', '=', max(n1, n2, n3, n4, n5))


# Task 9: 'Sort three'. Write a program that sorts three numbers from largest to smallest.

n1, n2, n3 = int(input()), int(input()), int(input())

print(max(n1, n2, n3))
print((n1 + n2 + n3) - max(n1, n2, n3) - min(n1, n2, n3))
print(min(n1, n2, n3))


# Task 10: 'Interesting number'. We call a number interesting if the difference between the maximum and minimum digits in it is equal to the average digit. Write a program that determines whether a number interesting or not. If the number interesting, you should print - 'Number of interesting' otherwise 'Number of uninteresting'.

n = int(input())

n1 = n // 100
n2 = (n // 10) % 10
n3 = n % 10

maxi = max(n1, n2, n3)
mini = min(n1, n2, n3)
aver = (n1 + n2 + n3) - maxi - mini

if (maxi - mini) == aver:
    print('Число интересное')
else:
    print('Число неинтересное')


# Task 11: 'Absolute amount'. Given five numbers. Write a program that calculates the sum of their moduli.

n1, n2, n3, n4, n5 = float(input()), float(input()), float(
    input()), float(input()), float(input())

print(abs(n1) + abs(n2) + abs(n3) + abs(n4) + abs(n5))


# Task 12: 'Manhattan distance'. Write a program that determines the Manhattan distance between two points whose coordinates are given.

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

print(abs(x1 - x2) + abs(y1 - y2))
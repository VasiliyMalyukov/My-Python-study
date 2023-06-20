# Lesson topic 'nested loops'

for i in range(1, 4):
    for j in range(3, 6):
        print(i, j)

print()

for i in range(1, 4):
    for j in range(3, 5):
        print(i + j, end='')

print()

counter = 0
for i in range(99, 102):
    temp = i
    while temp > 0:
        counter += 1
        temp //= 10
print(counter)

print()

# Task 1: 

n = int(input())

for i in range(1, n + 1):
    for j in range(3):
        print(n, end=" ")
    print()

# Task 2:

for i in range(1, int(input()) + 1):
    for j in range(5):
        print(i, end=" ")
    print()

# Task 3:

n = int(input())

for i in range(1, n + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print()

# Task 4:

n = int(input())
centr = n // 2 + 1
count = 0

for i in range(1, n + 1):
    if i > centr:
        count -= 1
    else:
        count += 1

    for _ in range(count):
        print('*', end='')
    print()

# Task 5:

n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print(i, end='')
    print()

# Task 6:

num = int(input())
count = 0
for y in range(1, num + 1):
    for x in range(y):
        count += 1
        print(count, end=' ')
    print()

# Task 7:

num = int(input())

for i in range(1, num + 1):
    count = 0
    for j in range(i):
        count += 1
        print(count, end='')
    for k in range(i, 1, -1):
        count -= 1
        print(count, end='')
    print()

# Task 8:

a, b = int(input()), int(input())
total_maximum = 0
digit = 0

for i in range(a, b + 1):
    maximum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            maximum += j
        if maximum >= total_maximum:
            total_maximum = maximum
            digit = j
print(digit, total_maximum)

# Task 9:

n = int(input())

for i in range(1, n+1):
    print(i, end='')
    for j in range(1, i+1):
        if i % j == 0:
            print('+', end='')
    print()

# Task 10:

n = int(input())

while n > 9:
    s = 0
    while (n > 0):
        last_digit = n % 10
        s += last_digit
        n = n // 10
    n = s
print(n)

# Task 11:

num = int(input())
total = 0
factorial = 1

for i in range(1, num+1):
    for j in range(1, i+1):
        factorial *= j
    total += factorial
    factorial = 1
print(total)

# Task 12:

a, b, = int(input()), int(input())
for i in range(a, b + 1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
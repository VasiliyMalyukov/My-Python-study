# Lesson topic 'while loop'

num = 12345
product = 1
while num != 0:
    last_digit = num % 10
    product = product * last_digit
    num = num // 10
print(product)

print()

num = 123456789
total = 0
while num != 0:
    last_digit = num % 10
    if last_digit > 4:
        total += 1
    num = num // 10
print(total)

# Task 1: 'Reverse Order 1'. Given a natural number. Write a program that prints its digits in
# a column in reverse order.

n = int(input())

while n != 0:
    last_digit = n % 10
    print(last_digit)
    n = n // 10

# Task 2: 'Reverse order 2'. Given a natural number. Write a program that reverses the order
# of the digits of a number.

n = int(input())

while n != 0:
    last_digit = n % 10
    print(last_digit, end='')
    n = n // 10

# Task 3: "Max and Min'. Given a natural number N. Write a program that determines its maximum
# and minimum digits.

n = int(input())
n_max = -1
n_min = 10

while n != 0:
    last_digit = n % 10
    if last_digit < n_min:
        n_min = last_digit
    if last_digit > n_max:
        n_max = last_digit
    n = n // 10

print('Максимальная цифра равна', n_max)
print('Минимальная цифра равна', n_min)

# Task 4: 'Together'. Given a natural number. Write a program that calculates:
# - the sum of its digits;
# - the number of digits in it;
# - the product of its digits;
# - the arithmetic mean of its digits;
# - its first digits;
# - the sum of its first and last digits.

n = int(input())

sum_n = 0
product = 1
total = len(str(n))
last_digit = n % 10
first_digit = n // (10 ** (total - 1))

while n != 0:
    m = n % 10
    sum_n += m
    product *= m
    n = n // 10
print(sum_n)
print(total)
print(product)
print(sum_n / total)
print(first_digit)
print(first_digit + last_digit)

# Task 5: 'Second digit'. Given a natural number N. Write a program that determines its second
# (from the beginning) digit.

n = int(input())

while len(str(n)) > 1:
    last_digit = n % 10
    n = n // 10

print(last_digit)

# Task 6: 'Same digits'. Given a natural number. Write a program that determines if a given
# number consists of the same digits.

n = int(input())
n_max = -1
n_min = 10

while n != 0:
    last_digit = n % 10
    if last_digit < n_min:
        n_min = last_digit
    if last_digit > n_max:
        n_max = last_digit
    n = n // 10

if n_max == n_min:
    print('YES')
else:
    print('NO')

# Task 7: 'Ordered numbers'. Given a natural number. Write a program that determines whether
# sequence of its digits, when viewed from right to left, is sorted in non-decreasing order.

n = int(input())
flag = True
last_digit1 = n % 10

while n != 0:
    last_digit = n % 10
    if last_digit >= last_digit1:
        last_digit1 = last_digit
    else:
        flag = False
    n = n // 10

if flag != True:
    print('NO')
else:
    print('YES')

# Lesson topic^ 'for' loop

for i in range(10):
    print('Привет')

print()

for i in range(5):
    num = int(input())
    print('Квадрат вашего числа равен:', num * num)
print('Цикл завершен')

# Task 1: 'Python is awesome'. Write a program that prints words 'Python is awesome!' 10 times.

for i in range(10):
    print('Python is awesome!')


# Task 2: 'Repeat after me 1'. Given a sentence and the number of times it must be repeated.
# Write a program that repeats the given sentence as many times as needed.

sentence, n = input(), int(input())

for i in range(n):
    print(sentence)

# Task 3: 'Character sequence'. Write a program that uses exactly three for loops to print
# the following sequence of characters:
# AAA
# AAA
# AAA
# AAA
# AAA
# AAA
# BBBB
# BBBB
# BBBB
# BBBB
# BBBB
# E
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# G

for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')

# Task 4: 'Star rectangle'. The input to the program is a natural number N. Write a program
# that prints a star rectangle with dimensions N * 19.

n = int(input())

for i in range(n):
    print('*' * 19)
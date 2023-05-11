# Lesson topic 'while loop'

i = 5
while i <= 12:
    print('Python awesome!')
    i += 1

print()

i = 7
a = 5
while i < 11:
    a += i
    i += 2
print(a)

# Task 1: 'Until END 1'. The input to the program is a sequence of words, each word on a separate
# line.The end of the sequence is the word "END" (without quotes). At the sane time, the word "END"
# itself is not included in the sequence, only symbolizing its end. Write a program that prints
# the terms of a given sequence.

text = input()

while text != 'КОНЕЦ':
    count = text
    text = input()
    print(count)

# Task 2: 'Until the END 2'. The input to the program is a sequence of words, each word on
# a separate line. The end of the sequence is the word "END" or "end" (capital or small letters,
# no quotes). At the same time, the words "END" and "end" themselves are not included in
# the sequence, only symbolizing its end. Write a program that prints the terms of a given
# sequence.

text = input()

while (text != 'КОНЕЦ') and (text != 'конец'):
    count = text
    print(count)
    text = input()

# Task 3: 'Number of members'. The input to the program is a sequence of words, each on a
# separate line. The end of the sequence is one of three words: "stop", "enough" (in small
# letters, without quotes). These words themselves are not included in the sequence, only
# symbolizing its end. Write a program that prints the total number of terms in a given sequence.

text = input()
count = 0

while (text != 'стоп') and (text != 'хватит') \
        and (text != 'достаточно'):
    count += 1
    text = input()
print(count)

# Task 4: 'While sharing'. The input to the program is a sequence of integers divisible by 7,
# each number on a separate line. The end of the sequence is any number that is not divisible
# by 7 (this number itself is not included in the sequence, only symbolizing its end).
# Write a program that prints the terms of a given sequence.

n = int(input())

while n % 7 == 0:
    print(n)
    n = int(input())

# Task 5: 'Sum of the numbers'. The input to the program is a sequence of integers, each number
# on a separate line. The end of the sequence is any negative number. Write a program that prints
# the sum of all terms in a given sequence.

n = int(input())
count = 0

while n >= 0:
    count += n
    n = int(input())
print(count)

# Task 6: 'Number of fives'. The input to the program is a sequence of integers from 1 to 5
# characterizing the student's grade, each number on a separate line. The end of the sequence is
# any negative number, or a number greater than 5. Write a program that displays the number
# of five.

n = int(input())
count = 0

while (n >= 0) and (n < 6):
    if n == 5:
        count += 1
    n = int(input())
print(count)

# Task 7: 'Pay the Witcher with minted coin'. Everyone knows that the Witcher is able to defeat
# any monsters, but his services will cost a lot, besides, the Witcher does not accept banknotes,
# he only accepts minted coins. In the world of the Witcher, there are coins with denominations
# 1, 5, 10, 25. Write a program that determines the minimum number of minted coins to be paid
# to the Witcher.

num = int(input())
count = 0

while num >= 25:
    count += 1
    num -= 25
while num >= 10:
    count += 1
    num -= 10
while num >= 5:
    count += 1
    num -= 5
while num >= 1:
    count += 1
    num -= 1
print(count)

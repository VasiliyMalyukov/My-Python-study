# Lesson topic: conditional operator

answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')
else:
    print('Не совсем так!')

print()

num1 = int(input())
num2 = int(input())

if num1 < num2:
    print(num1, 'меньше чем', num2)
if num1 > num2:
    print(num1, 'больше чем', num2)
if num1 == num2:                      # используем двойное равенство
    print(num1, 'равно', num2)
if num1 != num2:
    print(num1, 'не равно', num2)

print()

age = int(input())
if 3 <= age <= 6:
    print('Вы ребёнок')

print()

password1 = input()
password2 = input()

if password1 == password2:
    print('Пароль принят')
else:
    print('Пароль не принят')

print()

i = int(input())

if i % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

print()

numeric = int(input())

digit1 = numeric // 1000
digit2 = (numeric // 100) % 10
digit3 = (numeric // 10) % 10
digit4 = numeric % 10

if digit1 + digit4 == digit2 - digit3:
    print('ДА')
else:
    print('НЕТ')

print()

age = int(input())

if age >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

print()

a = int(input())
b = int(input())
c = int(input())

if (b - a) + b == c:
    print('YES')
else:
    print('NO')


print()

a = int(input())
b = int(input())

if a > b:
    print(b)
else:
    print(a)

print()

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a > b:
    ab = b
else:
    ab = a
    
if c > d:
    cd = d
else:
    cd = c

if ab > cd:
    print(cd)
else:
    print(ab)

print()

age = int(input())

if age <= 13:
    print('детство')
if 14 <= age <= 24:
    print('молодость')
if 25 <= age <= 59:
    print('зрелость')
if age >= 60:
    print('старость')

print()

a = int(input())
b = int(input())
c = int(input())

if a >= 0:
    a = a
else:
    a = 0

if b >= 0:
    b = b
else:
    b = 0

if c >= 0:
    c = c
else:
    c = 0

print (a + b + c)

print()
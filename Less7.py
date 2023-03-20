# Lesson topic: logical operators

age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
if age >= 12 and grade >= 7:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
    
print()

age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and city == 'Москва':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
    
print()

city = input('В каком городе вы живете?: ')
if city == 'Москва' or city == 'Санкт-Петербург' or city == 'Екатеринбург':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
    
print()

age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and (city == 'Москва' or city == 'Санкт-Петербург'):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
    
print()

age = int(input('Сколько вам лет?: '))
if not (age < 12):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
    
print()

num1 = 34
num2 = 81
if num1 // 9 == 0 or num2 % 9 == 0:
    print('число', num1, 'выиграло')
else:
    print('число', num2, 'выиграло')
    
print()

a = int(input())
if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5
p = (a + b) * (a + b)
print(p)

print()

x = int(input())

if -1 < x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')
    
print()

x = int(input())

if not(-3 < x < 7):
    print('Принадлежит')
else:
    print('Не принадлежит')
    
print()

x = int(input())

if (-30 < x <= -2) or (7 < x <= 25):
    print('Принадлежит')
else:
    print('Не принадлежит')
    
print()

n = int(input())

if 1000 <= n <= 9999:
    n = n
else:
    n = 1

if (n % 7 == 0) or (n % 17 == 0):
    print('YES')
else:
    print('NO')
    
print()

a = int(input())
b = int(input())
c = int(input())

if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    print('YES')
else:
    print('NO')
    
print()

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('YES')
else:
    print('NO')
    
print()

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if (a1 == a2) or (b1 == b2):
    print('YES')
else:
    print('NO')
    
print()

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if (-1 <= (a2 - a1) <= 1) and (-1 <= (b2 - b1) <= 1):
    print('YES')
else:
    print('NO')


    


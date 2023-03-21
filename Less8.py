# Lesson topic: conditional operator

x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print('Первая четверть')
    else:
        print('Четвертая четверть')
else:
    if y > 0:
        print('Вторая четверть')
    else:
        print('Третья четверть')
        
print()

grade = int(input('Введите вашу отметку по 100-балльной системе: '))

if grade >= 90:
    print(5)
else:
    if grade >= 80:
        print(4)
    else:
        if grade >= 70: 
            print(3)
        else:
            if grade >= 60:
                print(2)
            else:
                print(1)

print()

grade = int(input('Введите вашу отметку: '))

if grade >= 90:
    print(5)
elif grade >= 80:
    print(4)
elif grade >= 70:
    print(3)
elif grade >= 60:
    print(2)
else:
    print(1)

print()

a, b, c = int(input()), int(input()), int(input())
if a == b:
    if b == c:
        print(3)
    else:
        print(2)
else:
    if a == c:
        print(2)
    else:
        if b == c:
            print(2)
        else:
            print(0)

print()

a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b != c:
    print(2)
elif a != b == c:
    print(2)
elif a == c != b:
    print(2)
else:
    print(0)

print()

a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b != c or a != b == c or a == c != b:
    print(2)
else:
    print(0)
    
print()

n, k = int(input()), int(input())

if n > k:
    print('NO')
else:
    if k > n:
        print('YES')
    else:
        print("Don't know")

print()

a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print('Равносторонний')
else:
    if (a == b) or (a == c) or (b == c):
        print('Равнобедренный')
    else:
        print('Разносторонний')
        
print()

a, b, c = int(input()), int(input()), int(input())

if (a < b < c) or (c < b < a):
    print(b)
else:
    if (b < a < c) or (c < a < b):
        print(a)
    else:
        print(c)

print()

m = int(input())

if (m == 4) or (m == 6) or (m == 9) or (m == 11):
    print(30)
elif (m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) or (m == 12):
        print(31)
else:
    print(28)

print()

m = int(input())

if m < 60:
    print('Легкий вес')
elif 60 <= m < 64:
    print('Первый полусредний вес')
else:
    print('Полусредний вес')
    
print()

a, b, c = int(input()), int(input()), input()

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif (c == '/') and (b != 0):
    print(a / b)
elif (c == '/') and (b == 0):
    print('На ноль делить нельзя!')
else:
    print('Неверная операция')
    
print()

color1, color2 = input(), input()

if (((color1 == 'красный') or (color2 == 'красный')) or ((color2 == 'синий') or (color1 == 'синий')) or ((color2 == 'желтый') or (color1 == 'желтый'))) and (color1 == color2):
    print(color1)
elif ((color1 == 'красный') or (color2 == 'красный')) and ((color2 == 'синий') or (color1 == 'синий')):
    print('фиолетовый')
elif ((color1 == 'красный') or (color2 == 'красный')) and ((color2 == 'желтый') or (color1 == 'желтый')):
    print('оранжевый')
elif ((color2 == 'желтый') or (color1 == 'желтый')) and ((color2 == 'синий') or (color1 == 'синий')):
    print('зеленый')
else:
    print('ошибка цвета')
    
print()

x = int(input())

if (1 <= x <= 10) or (19 <= x <= 28):
    if x % 2 == 0:
        print('черный')
    else:
        print('красный')
elif (11 <= x <= 18) or (29 <= x <= 36):
    if x % 2 == 0:
        print('красный')
    else:
        print('черный')
elif x == 0:
    print('зеленый')
else:
    print('ошибка ввода')
    
print()

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if (a1 < a2 < b1) and (a1 < b2 < b1):
    print(a2, b2)
elif (a2 < a1 < b2) and (a2 < b1 < b2):
    print(a1, b1)
elif (a1 < a2 < b1) and (a2 < b1 < b2):
    print(a2, b1)
elif (a2 < a1 < b2) and (a1 < b2 < b1):
    print(a1, b2)
elif (a1 < a2) and (b1 == a2) and (b1 < b2):
    print(b1)
elif (a2 < a1) and (a1 == b2) and (b2 < b1):
    print(b2)
elif (a1 == a2) and (b1 == b2):
    print(a1, b1)
elif (a1 == a2) and (b1 < b2):
    print(a1, b1)
elif (a1 == a2) and (b2 < b1):
    print(a1, b2)
elif (b1 == b2) and (a1 < a2):
    print(a2, b1)
elif (b1 == b2) and (a2 < a1):
    print(a1, b1)
else:
    print('пустое множество')
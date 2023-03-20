b = int(input())
q = int(input())
n = int(input())
print(b * (q ** (n - 1)))
print()
sm = int(input())
print(sm // 100)
print()
people = int(input())
mandarins = int(input())
print(mandarins // people)
print(mandarins % people)
print()
n = int(input())
print((n + 1) // 2)
print()
seat = int(input())
print((seat + 3) // 4)
print()
minutes = int(input())
print(minutes, 'мин - это', minutes // 60, 'час',
      minutes - (minutes // 60) * 60, 'минут.')
print()
numeric = int(input())
digit1 = numeric // 100
digit2 = (numeric // 10) % 10
digit3 = numeric % 10
print('Сумма цифр =', digit1 + digit2 + digit3)
print('Произведение цифр =', digit1 * digit2 * digit3)
print()
abc = int(input())
a = abc // 100
b = (abc // 10) % 10
c = abc % 10
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')
print()
numeric = int(input())
digit1 = numeric // 1000
digit2 = (numeric // 100) % 10
digit3 = (numeric // 10) % 10
digit4 = numeric % 10
print('Цифра в позиции тысяч равна', digit1)
print('Цифра в позиции сотен равна', digit2)
print('Цифра в позиции десятков равна', digit3)
print('Цифра в позиции единиц равна', digit4)
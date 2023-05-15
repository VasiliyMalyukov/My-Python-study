# Lesson topic 'break, continue, else'

num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False
        break               # останавливаем цикл если встретили делитель числа

if flag == True:
    print('Число простое')
else:
    print('Число составное')

print()

result = 0
for i in range(10):
    num = int(input())
    if num < 0:
        break
    result += num
print(result)

print()

num = int(input())
number = num
flag = False
while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        flag = True
        break        # прерываем цикл, так как число гарантированно содержит цифру 7
    num //= 10

if flag == True:
    print('Число', number, 'содержит цифру 7')
else:
    print('Число', number, 'не содержит цифру 7')

print()

for i in range(1, 101):
    if i == 7 or i == 17 or i == 29 or i == 78:
        continue  # переходим на следующую итерацию
    print(i)

print()

mult = 1
for i in range(1, 11):
   if i % 2 == 0:
      continue
   if i % 9 == 0:
      break
   mult *= i
print(mult)

# Task 1: 'Smallest divisor'. The input to the program is a number N. Write a program that
# outputs its smallest difference from 1 divider.

n = int(input())
a = 2

while a <= n:
    if n % a == 0:
        print(a)
        break
    a += 1

# Task 2: 'Follow the rules'. The input to the program is a natural number N. Write a program that
# prints numbers from 1 to N inclusive except for:
# - numbers from 5 to 9 inclusive;
# - numbers from 17 to 37 inclusive;
# - numbers from 78 to 87 inclusive.


n = int(input())

for i in range(1, n + 1):
    if (5 <= i <= 9) or (17 <= i <= 37) or (78 <= i <= 87):
        continue
    print(i)


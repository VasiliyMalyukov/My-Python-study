# Lesson topic: string data type

#s1 = 'abcdef'
#length1 = len(s1)               # считаем длину строки из переменной s1
#length2 = len('Python rocks!')  # считаем длину строкового литерала
#print(length1)
# print(length2)

#print()

#num1 = 1777    # целое число
#num2 = 17.77   # число с плавающей точкой
#s1 = str(num1) # преобразовали целое число в строку '1777'
# s2 = str(num2) # преобразовали число с плавающей точкой в строку '17.77'

#print()

#s1 = 'ab' + 'bc'
#s2 = 'bc' + 'ab'
#s3 = s1 + s2 + '!!'
#print(s1)
#print(s2)
# print(s3)

#print()

#print('a', 'b', 'c', sep='*', end='!')
#print()  # переход на новую строку
#print('a' + '*' + 'b' + '*' + 'c' + '!')

#print()

#mystr = 'да'
#mystr = mystr + 'нет'
#mystr = mystr + 'да'
#print(mystr)

#print()

#str1 = '1'
#str2 = str1 + '2' + str1
#str3 = str2 + '3' + str2
#str4 = str3 + '4' + str3
#print(str4)

#print()

#mystr = '123' * 3 + '456' * 2 + '789' * 1
#print(mystr)

#print()

# Task 1: Write a program that prints text: "Python is a great language!", said Fred. "I don't ever remember having this much fun before."

#print('''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')


# Task 2: 'What's Your Name?'. Write a program that reads two lines from the keyboard - the user's first and last name and outputs the phrase: «Hello [entered name] [last name entered]! You just delved into Python».

#name = input()
#last_name = input()

#print('Hello', name, last_name + '!', 'You just delved into Python')


# Task 3: 'Football team'. Write a program that reads the name of a football team from the keyboard and prints out the phrase: "The football team [input string], has a lenght of [input string lenght] characters" in Russian languege.

name_team = input()
lenght_name = len(name_team)

print('Футбольная команда', name_team, 'имеет длину', lenght_name, 'символов')


# Task 4: 'Three cities'. The names of three cities are given. Write a program that determines the shortest and longest city names
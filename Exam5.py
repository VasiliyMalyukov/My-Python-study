# Exam 5: conditional operator

# Task 1: Write a program that determines if a year with a given number ends in two zeros. If the year ends, then print "YES", otherwise print "NO".

year = int(input())

if (year % 100) == 0:
    print('YES')
else:
    print('NO')

# Task 2: 'Chess board'. Two cells of a chessboard are given. Write a program that determines whether the specified cells have the same color or not. If they are of the same color, then print the word "YES", and if they are of different colors, then print "NO".

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if ((x1 + x2 + y1 + y2) % 2) == 0:
    print('YES')
else:
    print('NO')

# Task 3: 'Girls only'. The football team recruits girls from 10 to 15 years old inclusive. Write a program that queries the age and gender of an applicant using the gender designation letters m (from male - male) and f (from female - female) and determines whether the applicant is suitable for joining the team or not. If the applicant is suitable, then print "YES", otherwise print "NO".

age, gender = int(input()), input()

if (10 <= age <= 15) and (gender == 'f'):
    print('YES')
else:
    print('NO')

# Task 4: 'Roman numerals'. Write a program that reads in integer and outputs its corresponding Roman numeral. If the number in outside the range 1-10, then the program shold display the text 'error'.

#numeric = int(input())

if numeric == 1:
    print('I')
elif numeric == 2:
    print('II')
elif numeric == 3:
    print('III')
elif numeric == 4:
    print('IV')
elif numeric == 5:
    print('V')
elif numeric == 6:
    print('VI')
elif numeric == 7:
    print('VII')
elif numeric == 8:
    print('VIII')
elif numeric == 9:
    print('IX')
elif numeric == 10:
    print('X')
else:
    print('ошибка')
    
# Task 5: 'YES or NO that is the question'. Write a program that takes a number as input and aoutputs the text 'YES' or 'NO' depending on the conditions. Conditions:
# 1) If the number is odd, then output 'YES';
# 2) If the number is even in the range from 2 to 5 (inclusive), then output 'NO';
# 3) If the number is even in the range from 6 to 20 (inclusive), then output 'YES';
# 4) If the numer is even and greater than 20, then print 'NO'.

n = int(input())
if ((n % 2) != 0) or (6 <= ((((n % 2) == 0) * 0) + n) <= 20):
    print('YES')
else:
    print('NO')
    
# Task 6: 'Elephant move'. Two different cells of chessboard are given. Write a program that determines if the bishop can move from the first cell to the second in one move. The program receives as input four numbers from 1 to 8 each, specifying the column number and row number, first for the first cell, then for the second cell. The program should print 'YES' if it is possible to get to the second from the first cell by the bishop's move, or 'NO' otherwise.

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 + y1) == (x2 + y2):
    print('YES')
elif (x2 - x1) == (y2 - y1):
    print('YES')
elif (x1 - x2) == (y1 - y2):
    print('YES')
else:
    print('NO')

# Task 7: 'Knight's move'. Two different cells of a chessboard are given. Write a program that determines if the knight can get from the first cell to the second in one move. The program receives as input four numbers from 1 to 8 each, specifying the column number and row number, first for the first cell, then for the second cell. The program should print 'YES' if it is possible to get to the second one from the first cell by knight's move, or 'NO' otherwise.

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (((x1 + y1) - (x2 + y2)) == 1) and ((x2 == (x1 + 1)) or (y2 == (y1 + 1))):
    print('YES')
elif (((x1 + y1) - (x2 + y2)) == -1) and ((x2 == (x1 + 2)) or (y2 == (y1 + 2))):
    print('YES')
elif (((x1 + y1) - (x2 + y2)) == 3) and ((x2 == (x1 - 1)) or (y2 == (y1 - 1))):
    print('YES')
elif (((x1 + y1) - (x2 + y2)) == -3) and ((x2 == (x1 + 2)) or (y2 == (y1 + 2))):
    print('YES')
else:
    print('NO')

# Task 8: 'Queen move'. Two different cells of a chessboard are given. Write a program that determines if the queen can get from the first cell to the second in one move. The program receives as input four numbers from 1 to 8 each, specifying the column number and row number, first for the first cell, then for the second cell. The program should print 'YES' if it is possible to get to the second one from the first cell by the queen's move, or 'NO' otherwise.

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 + y1) == (x2 + y2):
    print('YES')
elif (x2 - x1) == (y2 - y1):
    print('YES')
elif (x1 - x2) == (y1 - y2):
    print('YES')
elif (-1 <= (x2 - x1) <= 1) and (-1 <= (y2 - y1) <= 1):
    print('YES')
elif (x1 == x2) or (y1 == y2):
    print('YES')
else:
    print('NO')




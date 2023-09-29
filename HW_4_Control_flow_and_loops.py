# Practice section 1

# Figure out the result of the following expressions:
'''
a) (1 <= 1) and (1 != 1)
    True and False
    False
b) not (1 != 2)
    not True
    False
c) ("good" != "bad") or False
    True or False
    True
d) ("good" != "Good") and not (1 == 1)
    True and not True
    False
'''

# Make all of them True by adding parentheses:
'''
a) False == not True
    False == (not True)
b) True and False == True and False
    True and (False == (True and False))
    (True and False) == (True and False)
c) not True and "A" == "B"
    not (True and ("A" == "B"))
    not (True and "A" == "B")
'''

# Task 1. Even or odd. Прийняти від користувача число, вивезти чи even/odd
num = input('Input number: ')
if num.isdigit() or (num[0] == '-' and num[1:].isdigit()):
    num = int(num)
    result = 'even' if num % 2 == 0 else 'odd'
    print(result)
else:
    print('Wrong input')

# Task 2. When provided with a number between 0-9, return it in words. Input :: 1 Output :: "One".
# With match
num = input('Input number between 0-9: ')
if num.isdigit():
    match num:
        case '0':
            print('Zero')
        case '1':
            print('One')
        case '2':
            print('Two')
        case '3':
            print('Three')
        case '4':
            print('Four')
        case '5':
            print('Five')
        case '6':
            print('Six')
        case '7':
            print('Seven')
        case '8':
            print('Eight')
        case '9':
            print('Nine')
        case _:
            print('Try again')
else:
    print('Input error')


# With loop
num = input('Input number between 0-9: ')
if num.isdigit():
    if num == '0':
        print('Zero')
    elif num == '1':
        print('One')
    elif num == '2':
        print('Two')
    elif num == '3':
        print('Three')
    elif num == '4':
        print('Four')
    elif num == '5':
        print('Five')
    elif num == '6':
        print('Six')
    elif num == '7':
        print('Seven')
    elif num == '8':
        print('Eight')
    elif num == '9':
        print('Nine')
    else:
        print('It\'s not a number between 0 and 9')
else:
    print('It\'s not a number between 0 and 9')


# Task 3. Прийняти від користувача два числа і отримати дію над цими числами. Реалізувати +,-, /, *, /, **
num_1, num_2, des = input('Input number: a = '), input('Input number: b = '), input('Input arithmetic operation: ')
if (num_1.isdigit() and num_2.isdigit) or ((num_1[1:].isdigit() and num_2[1:].isdigit)):
    num_1, num_2 = int(num_1), int(num_2)
    match des:
        case '+': print('a + b =', num_1 + num_2)
        case '-': print('a - b = ', num_1 - num_2)
        case '*': print('a * b = ', num_1 * num_2)
        case '/': print('a / b = ', num_1 / num_2)
        case '**': print('a ** b = ', num_1 ** num_2)
        case _: print('Bad input')
else:
    print('Bad input')


# Task 4. Прийняти від користувача name, surname. Вивезти ініціали.
name = input('Input name: ')
surname = input('Input surname: ')
init = f'{name[0]}.{surname[0]}'
print('Name:', name, 'Surname:', surname, 'Init:', init)


# Practice section 2

# 1. Write a Python program that reads two integers representing a month and prints the season for that month. Get month from the user input.
# Expected Output:
# Input the month: october
# Season is autumn'''

month = input('Input number of month : ')
match month:
    case '01': print('Input the month: January \
        \nSeason is winter')
    case '02': print('Input the month: February \
        \nSeason is winter')
    case '03': print('Input the month: March \
        \nSeason is spring')
    case '04': print('Input the month: April \
        \nSeason is spring')
    case '05': print('Input the month: May \
        \nSeason is spring')
    case '06': print('Input the month: June \
        \nSeason is summer')
    case '07': print('Input the month: July \
        \nSeason is summer')
    case '08': print('Input the month: August \
        \nSeason is summer')
    case '09': print('Input the month: September \
        \nSeason is autumn')
    case '10': print('Input the month: October \
        \nSeason is autumn')
    case '11': print('Input the month: November \
        \nSeason is autumn')
    case '12': print('Input the month: December \
        \nSeason is winter')
    case _: print('I don\'t know what you mean')


# 2. Write a Python program to get next day of a given date.
# Get day, month and year from the user input.
# Expected Output:
# **Input a year:** 2022
# **Input a month [1-12]:** 8
# **Input a day [1-31]:** 23
# The next date is [yyyy-mm-dd] 2022-8-24

year = input('Input a year: ')
month = input('Input a month [1-12]: ')
day = input('Input a day [1-31]: ')
if year.isdigit() and month.isdigit() and day.isdigit():  # первіряємо, що ввели числа
    year, month, day = int(year), int(month), int(day)
    if month in range(1, 13) and day in range(1, 32):  # перевіряємо, що числа з потрібного діапазону

        # визначаємо довжину місяця
        if month in (1, 3, 5, 7, 8, 10, 12):
            len_month = 31
        elif month == 2:
            # визначаємо високосний рік
            if (year % 4 == 0):
                len_month = 29
            else:
                len_month = 28
        else:
            len_month = 30

        # визначаємо наступний день
        if day < len_month:
            next_day = day + 1
            next_date = f'{year}-{month}-{next_day}'
            print('The next date is [yyyy-mm-dd] ', next_date)
        elif day == len_month:
            next_day = 1
            if month == 12:
                next_year = year + 1
                next_month = 1
                next_date = f'{next_year}-{next_month}-{next_day}'
            else:
                next_month = month + 1
                next_date = f'{year}-{next_month}-{next_day}'
            print('The next date is [yyyy-mm-dd] ', next_date)
        else:
            print('Bad input')
    else:
        print('Bad input')
else:
    print('Bad input')


# 3. Get a phrase from user input. Display whether the lenght of the string if longer than 5 characters, equal to 5 characters or shorter than 5 characters. Use if, elif, else for this.
phrase = input('Input phrase: ')
if len(phrase) > 5:
    print('Lenght of the phrase longer than 5 characters')
elif len(phrase) == 5:
    print('Lenght of the phrase equal 5 characters')
else:
    print('Lenght of the phrase shoter than 5 characters')


# 4. Get a positive number from user input. Find all factors of this number.
# Example:
# If the number is 6, the factors are: 1, 2, 3, 6
# If the number is 10, the factors are: 1, 2, 5, 10

num = input('Input a positive number: ')
if num.isdigit():
    num = int(num)
    for i in range(1, num):
        if num % i == 0:
            print(i, end=', ')
    print(num)
else:
    print('Bad input')


# 5. Write a Python program to check a triangle is equilateral, isosceles or scalene. Get all three sides from user input.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.'''

side_1, side_2, side_3 = input('Input side one, a = '), input('Input side two, b = '), input('Input side three, c = ')
if side_1.isdigit() and side_2.isdigit() and side_3.isdigit():
    side_1, side_2, side_3 = int(side_1), int(side_2), int(side_3)
    if (side_1 < side_2 + side_3) and (side_2 < side_1 + side_3) and (side_3 < side_1 + side_2):
        if side_1 == side_2 == side_3:
            print('Triangle is equilateral')
        elif (side_1 == side_2) or (side_2 == side_3) or (side_1 == side_3):
            print('riangle is isosceles')
        else:
            print('riangle is scalene')
    else:
        print('Triangle does\'n exist')
else:
    print('Bad input')


# Practice section 3:
# 1. Write a for loop that prints out the integers from 2 to 10, each on a new line, by using the range() function.
for i in range(2, 11):
    print(i)

# 2. Use a while loop that prints out the integers from 2 to 10
i = 2
while i <= 10:
    print(i)
    i += 1

# 3. Write a program that takes number as its input and doubles that number few times in a loop. Number of iterations and initial number should be taken from user input. You should display each result on a separate line. Here is some sample output:
''' Input:
initial number: 2
number of iterations: 5

Output:
4
8
16
32
64
'''

number = input('Input number: ')
iter = input('Input number of iteration: ')
if number.isdigit() and iter.isdigit():
    num = int(number)
    iter = int(iter)
    for i in range(iter):
        num *= 2
        print(num)
else:
    print('Wrong input')

# 4. Write a program that caluculate Fibonacci series. The Fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers.
# The first two numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth number is 1 + 2 = 3, and so on. Number of iterations should be taken from user input.
n_iter = input('Input number of iterations: ')
n_iter = int(n_iter) if n_iter.isdigit() else print('Bad input')
a = 1
print(a)
b = 1
print(b)
for i in range(n_iter-1):
    c = a + b
    print(c)
    a = b
    b = c


# 5. Write a program that takes a number as input and revert it using math operators.
# You might use result of the exercise from the first lesson. Here you should be able to do it not only for three-digit numbers, but for any numbers.
num = input('Input number: ')
num_reverse = 0
if num.isdigit():
    num = int(num)
    # визначаємо кількість останніх нулів у числі
    null = 0
    num_zero = num
    while num_zero % 10 == 0:
        null += 1
        num_zero = num_zero // 10
    # розвертаємо число
    while num > 0:
        digit = num % 10
        num = num // 10
        num_reverse = num_reverse * 10 + digit
    # якщо введене число закінчувалося нулями, то виводимо їх на друк
    if null != 0:
        print('0'*null + str(num_reverse))
    else:
        print(num_reverse)
else:
    print('Bad input')

# Інший способ розвернути число, за допомогою розкладу числа за степенями числа 10
num = input('Input number: ')
num_reverse = 0
if num.isdigit():
    num = int(num)
    # визначаємо кількість останніх нулів у числі
    null = 0
    num_zero = num
    while num_zero % 10 == 0:
        null += 1
        num_zero = num_zero // 10
    # розвертаємо число
    i = 0
    for digit in num:
        digit = int(digit)
        num_reverse += digit * 10 ** i
        i += 1
    # якщо введене число закінчувалося нулями, то виводимо їх на друк
    if null != 0:
        print('0'*null + str(num_reverse))
    else:
        print(num_reverse)
else:
    print('Bad input')


# Practice section 4
# 1. Write a program that always asks user to input somethings. Quit only if user inputs 'q' or 'Q'.
str = input('Input something: ')
while str.lower() != 'q':
    str = input('Input something: ')

# 2. Write a program that iterated from 0 to 100 and prints out the number if it is divisible by 3.
for i in range(101):
    if i % 3 != 0:
        continue
    print(i)


# 3. Get a number from user input and iterate from 0 to that number.
# Print 'foo' if the number is divisible by 3.
# Print 'bar' if the number is divisible by 5.
# Print 'foobar' if the number is divisible by both 3 and 5.'''
num = input('Input number: ')
if num.isdigit():
    num = int(num)
    for i in range(num + 1):
        if i % 15 == 0:
            print('foobar')
        elif i % 3 == 0:
            print('foo')
        elif i % 5 == 0:
            print('bar')
        else:
            print(i)

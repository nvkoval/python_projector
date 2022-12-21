'''import sys
import random
print(f"Version of you system: {sys.version.split(' ')[0]}")
print(f"0 - {bool(0)}, 1 - {bool(1)}, строка - {bool('a')}, пуста строка - {bool('')}")
salary = 10_000
print(salary <= 7000 or salary == 10_000)
print(12 < 13 or 3 ** '6')
print('not True: ', not True)
print('not False: ', not False)
print('not True == False: ', not True == False)
print(True and not (3 != 3.0))
a1 = (3 != 3.0)
print(a1)
print(True and not True)
print(("C" != "C") or not (23 >= 34))
print(False or not False)

numbers = 80
if numbers >= 18: # Перевірка умови, якщо True то переходить в блок коду, інші пропускає
    print('You can go bar')
elif numbers <= 0:
    print('You are not yet born')
elif numbers >= 100:
    print('Wrong age')
elif numbers >= 0 and numbers <= 18:
    print(f'Wait to go bar {18 - numbers} year')
else:
    print('Try again')


### Ternar operator - work with 3 operands
age =  45
vote = True if age >= 18 else False # Спочатку що повинно повернути, if умова else все що в іншому випадку 
print(vote)


age =  15
number = 20
vote = True if age >= 18 else \
    True if number == 15 else 'Test' # Спочатку що повинно повернути, if умова else все що в іншому випадку 
print(vote)
'''
name_of_user = 'Sasha'
age_of_user = 18
des = 'print'
match des:
    case 'print':
        print(f'Hello {name_of_user} \nYou {age_of_user} years old')
    case 'play':
        print("Play music")
    case _ :
        print('I don\'t know what you want')


'''# Task 1. Even or odd. Прийняти від користувача число, вивезти чи even/odd
num = int(input('Input number:'))
if num % 2 == 0:
    print('even')
else: print('odd')'''


'''# Task 2. When provided with a number between 0-9, return it in words. Input :: 1 Output :: "One".
num = input('Input number between 0-9: ')
if num.isdigit :
    print('False input')
elif num == 0:
    print('Zero')
elif num == 1: 
    print('One')
elif num == 2: 
    print('Two')
elif num == 3: 
    print('Three')
elif num == 4: 
    print('Four')
elif num == 5: 
    print('Five')
elif num == 6: 
    print('Six')
elif num == 7: 
    print('Seven')
elif num == 8: 
    print('Eight')
elif num == 9: 
    print('Nine')'''

# Task 3. Прийняти від користувача два числа і отримати дію над цими числами. 
# Реалізувати +,-, /, *, /, ** 

'''Explain:
   user_input = 6
   user_second_input = 10
   des = '+'
Result:
    print(user_input + user_second_input = 16(result))
'''
# Task 4. Прийняти від користувача name, surname. Вивезти ініціали. 
name = input('Input name: ')
surname = input('Input surname: ')
init_name = name[0]
init_surname = surname[0]
init = init_name + '.' + init_surname
print('Name:', name, 'Surname:', surname, 'Init:', init)
'''Explain:
    name = 'Name'
    surname = 'Surname'
Result:
    print(Name: Name, Surname: Surname, Init: N.S)'''

'''iteration = 1
while iteration <= 5: # умова припинення виконання
    print(iteration)
    iteration += 1 # змінуємо нашу змінну щоб цикл могли вийти із циклу
    
print('End')

num = float(input("Enter a positive number: "))
while num <= 0:
    print("That's not a positive number!")
    num = float(input("Enter a positive number: "))

print("Good job!")


word = "Projector"
index = 0
while index < len(word): # Умова для проходження по ітер  типу даних
    print('Current letter:', word[index]) # Звертаємось до символу під індексом
    index = index + 1

name = 'Some name'
for i in name:
    print(i)

test_range = range(0, 10, 3) # Якщо один параметр - то повино бути значення до куди(stop)
for i in test_range:
    print(i)

string = 'Stop iteration when find % more text we can\'t see'
print(string)

for i in string:
    if i == '%':
        print('%' * 45)
        break # stop loop and go next 
    print(i)
print('End loop and go next stage')

a = 15
print(f'After loop create a {a}')

for i in range(0, 30):
    if i % 5 == 0 or i % 10 == 0 :
        continue # Пропускає дану умову і повертається на початок 
    print(i)

for i in range(5):
    print(i)
else:
    print('The for loop is over')

'''

# 1. Write a for loop that prints out the integers from 2 to 10, 
# each on a new line, by using the range() function.
'''for i in range(2, 11):
    print(i)'''

# 2. Use a while loop that prints out the integers from 2 to 10
'''i = 2
while i<=10:
    print(i)
    i += 1'''

 # 3. Write a program that takes number as its input and doubles that number few times in a loop. 
 # Number of iterations and initial number should be taken from user input. 
 # You should display each result on a separate line. 
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

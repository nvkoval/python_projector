# While - loop
# Task 1. Знайти помилку. Описати що робить код, бажано построчно 
'''pointer = 0 # задаємо початкове значення змінної
counter = input('Enter number') # помилка 'iput'
counter = int(counter) # для порівняння потрібно перетворити у число
while pointer <= counter: 
    print(f'Step {pointer} to {counter}') # помилка в написанні poiter
    pointer += 1 # збільшуємо на одиницю значення, але треба pointer, а не counter

'''
# # Task 2. Знайти суму чисел від 0 до 100
'''sum_ = 0
for i in range(100):
    sum_ += i
print(sum_)'''

# Task 3. Розвернути строку 1. за допомогою цикла 2. Функцією . Example: 123 -> 321
'''str = input('Input string: ')
i = len(str) 
res = ''
for i in range(i, 0, -1):
    i -= 1
    res += str[i]
print(res)'''
     

#str_reverse = str[::-1] # slice 


# Task 4. Порахувати сумму чисел, введену user. Example: 123 -> 
'''num = input('Input number')
sum_digit = 0
for i in num:
    sum_digit += int(i)
print(sum_digit)'''

# Test task 
'''Create the dictionary with numbers (counts) of vowels in the given string in one line. 
We consider a, e, i, o, u as vowels (not y).

Example of input: 'Education'
Example of output: count of  vowels: 5 * Потрібно порахувати vowels і вивезти їх кількість'''
'''str = input('Inout string: ')
count_vowels = 0
for vow in 'aeiou':
    if vow in str: 
        count_vowels += 1
print('Всього голосних у строці', count_vowels)'''


'''
def add(a, b) -> int: # Створити функцію з двома параметрами, порядок передачі аргументів важливий!
    print(f'A = {a} B = {b}')
    return a + b

result = add(5, 7)
print(result)'''

'''a, b = 15, True

def minus(a, b):
    print(f'A = {a} B = {b}')
    return a - b

print(minus(16, 18))'''


'''def sum_of_two_numbers(a, b):  # signature
    # body
    sum_result = a + b
    return sum_result
    # print(f'Result is {sum_result}')


result = sum_of_two_numbers(1, 2)
print(result)
print(sum_of_two_numbers(30, 50))
print('a=', 1, 'b=', 2, 'sum_of_two_numbers(1,2)', sum_of_two_numbers(1,2))'''
'''
def get_int_from_input():  # signature
    # body
    input_value = input('input something')
    return int(input_value)
    print(f'Result is {sum_result}')


result = get_int_from_input()
print(result, '*')'''

'''def all_math(a, b, operation):
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        case _ :
            return None

print(all_math(5, 10, '-'))
'''

# Task 5. Створити функцію, і вивезти сумму чисел від 0 до числа який введе користувач.
'''
def sum_of_number(user_number):
    sum_of_number = 0
    for i in range(user_number):
        sum_of_number += i
    return (sum_of_number)

user_number = int(input('Enter number: '))
    
print(sum_of_number(user_number))
'''
# Task 6. Створити функцію, яке повертає сумму чисел від 0 до числа який введе користувач, 
# числа повинні бути even
'''def sum_of_number(user_number):
    sum_of_number = 0
    for i in range(0, user_number, 2):
        sum_of_number += i
    return (sum_of_number)

user_number = int(input('Enter number: '))
    
print(sum_of_number(user_number))'''



# Опціальні параметри 
'''def try_option(result = 'Hello'):
    print(f'Result: {result}')
print(try_option(), try_option('My hello'))
'''

'''def try_option_with_name(surname, name = 'User'):
    print(f'Hello {name} {surname}')

#try_option_with_name()
try_option_with_name('Ukr')'''

'''def multiply_two_numbers(
    zero_argument,
    first_argument = '2',
    second_argument = '3'
):  # signature
    # body
    sum_result = zero_argument + first_argument +  second_argument
        
    return sum_result

result = multiply_two_numbers('1', second_argument='4')
print(result)'''

# types
# Для того щоб вказати тип через : вказуємо тип, для того щоб вказати очікуваний тип -> після цього вказуємо тип
'''def sum_values(first_value: int, second_value: int) -> int:
    return first_value + second_value

print(sum_values('4', '5'), sum_values(5,10))'''

'''def read(a: bool = 'Hello'):
    print(a)'''

# *args
'''def function_with_args(*args):
    sum(args)
    print(f'args: {sum(args)}')
function_with_args(1, 2, 3, 4, 5, 6)'''

# *args
'''def function_with_args(param1, param2, param3 ,*args):
    print(f'Param1 = {param1}')
    print(f'Param2 = {param2}')
    print(f'Param3 = {param3}')
    print(f'Param args = {args}')
    
    sum(args)
    print(f'args: {sum(args)}')
function_with_args(1, 2, 3, 4, 5, 6)'''

'''Task 1. Дискримінант. Створіть функцію з іменем discriminant.
Функція повинна приймати на вхід a, b, c, choose. Де a, b, c - це аргументи функції, choose - опціональний параметр, вибору способу рішення(дискримінант або Вієта, 1 - disc, 2 - Вієта) 
Функція повинна повертати в залежності від параметрів один/два кореня або їх відсутність.
Example:
Input: a = 5, b = -8, c = 3 
Output: x = 1, x = 0.6 Результати округлювати до 2 знаку. Функція повинна перевіряти тип аргументів(int повинен бути).'''

def disc(a, b, c) -> int:
    if a ==0 :  
        print('Bad input')
         
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b - D**0.5) / (2*a)
        x2 = (-b + D**0.5) / (2*a)
    elif D == 0:
        x1 = x2 = -b / (2*a)

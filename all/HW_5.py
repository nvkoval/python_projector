# Practice section 1:

# 1. Write a program that caluculate Fibonacci series.
# The Fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers.
# The first two numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth number is 1 + 2 = 3, and so on. Number of iterations should be taken from user input.
def fibonacci(n_iter):
    n_iter = int(n_iter) if n_iter.isdigit() else print('Bad input')
    a = 1
    fib = str(a)
    b = 1
    fib += f', {str(b)}'
    for i in range(n_iter-1):
        c = a + b
        fib += f', {str(c)}'
        a = b
        b = c
    return fib


n_iter = input('Input number of iterations: ')
print(fibonacci(n_iter))


# Practice section 2
# 1. Write a program that iterated from 0 to 100 and prints out the number if it is divisible by 3.
def num_div_by_3(n=100):
    all_num = ''
    for i in range(n+1):
        if i % 3 != 0:
            continue
        all_num += f'{str(i)}, '
    return all_num


print(num_div_by_3())

# 2. Get a number from user input and iterate from 0 to that number.
# Print 'foo' if the number is divisible by 3.
# Print 'bar' if the number is divisible by 5.
# Print 'foobar' if the number is divisible by both 3 and 5.


def num_div_by_3_5_15(num):
    if num.isdigit():
        num = int(num)
        for i in range(num + 1):
            r_3 = i % 3
            r_5 = i % 5
            if r_3 == 0 and r_5 != 0:
                print('foo')
            elif r_3 != 0 and r_5 == 0:
                print('bar')
            elif r_3 == 0 and r_5 == 0:
                print('foobar')
            else:
                print(i)


num = input('Input number: ')
print(num_div_by_3_5_15(num))


# Practice block 3:
# 1. Write a function called square() with one argument of int type and returns the value of that number raised to the second power.
def square(input_num: int) -> int:
    return input_num ** 2


input_num = int(input('Input integer number: '))
print(square(input_num))

# 2. Write a program called convert_cel_to_fahr() that takes a temperature in Celsius and returns the equivalent temperature in Fahrenheit. It should take a number as an argument from user input and return a number to the console.


def convert_cel_to_fahr(temp_cels: int):
    return (temp_cels * 9/5) + 32


print(convert_cel_to_fahr(16))

# 3. Write a function that implement case swapping. It should return the same result as swapcase() method. Your function should accept one str argument and convert all lower case values to upper case and vice versa.
# def swapcase(input_string: str) -> str:
#     do something
# print(swapcase('HelLo'))
# > 'hELlO


def swapcase(input_string: str) -> str:
    swapcase_string = ''
    for letter in input_string:
        if letter.islower():
            swapcase_string += letter.upper()
        else:
            swapcase_string += letter.lower()
    return swapcase_string


print(swapcase('HelLo'))

# Task 1. Дискримінант. Створіть функцію з іменем discriminant.
# Функція повинна приймати на вхід a, b, c, choose. Де a, b, c - це аргументи функції, choose - опціональний параметр, вибору способу рішення(дискримінант або Вієта, 1 - disc, 2 - Вієта)
# Функція повинна повертати в залежності від параметрів один/два кореня або їх відсутність.

# Example:
# Input: a = 5, b = -8, c = 3
# Output: x = 1, x = 0.6 Результати округлювати до 2 знаку. Функція повинна перевіряти тип аргументів(int повинен бути).

# Крок 1: допустимі типи, isinstance, type, [int, float, bool]
# Крок 2: Ділення на 0, etc....
# Крок 3: без бібліотек!!!!
# Крок 4: Оптимальність
# Крок 5: перевірка назв
# Крок 6: побітові операції + винагорода
# Крок 7: Обмеженна 3 ступені
# Крок 8: тільки цикли, функції, строки-числа, built-in-function(sum, len) можна


def discriminant(a: int, b: int, c: int, choose=1):

    # розв'язання через дискриминант
    def disc():
        D = b**2 - 4*a*c
        print(f'D = {D}')

        if D > 0:
            x1 = (-b - D**0.5) / (2*a)
            x2 = (-b + D**0.5) / (2*a)
            result = f'x1 = {round(x1, 2)}, x2 = {round(x2, 2)}'
            return result
        elif D == 0:
            x = -b / (2*a)
            result = f'x1 = x2 = {round(x, 2)}'
            return result
        else:
            result = 'Дійсних коренів немає, D < 0'
            return result

    # роз'язання за допомогою теореми Вієта, виводить суму та добуток коренів
    def viet():
        mult_x = c / a
        sum_x = -b / a
        result = f'x1 + x2 = {round(sum_x, 2)}, x1 * x2 = {round(mult_x, 2)}'
        return result

    # перевірка типів введених даних
    if isinstance(a, (int, float, bool)) and isinstance(b, (int, float, bool)) and isinstance(c, (int, float, bool)):

        # виключення ділення на нуль
        if a == 0:
            return 'а = 0, це не квадратне рівняння'
        else:

            # відповідного до введеного параметру choose розв'язуємо або дискриминантом, або за теоремою Вієта
            match choose:
                case 1:
                    return disc()
                case 2:
                    return viet()
                case _:
                    return 'Bad input'
    else:
        return 'Bad input'


print(discriminant(5, -8, 3))
print(discriminant(5, -8, 3, choose=2))

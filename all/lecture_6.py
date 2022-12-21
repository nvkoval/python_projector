'''x = 5

def function():
    x = 2
    print(f'Inside function x = {x}')
    
function()
print(f'Outside function x = {x}')'''

'''x = 2

def outer_func():
    y = 3
    def inner_func():
        j = 5
        return x + y + j
    
    return inner_func()

result = outer_func()
print(f'Result is {result}')'''

'''total = 0
def add_to_total(n):
    total1 = total + n
    return total1

print(add_to_total(5))
print(total)'''


'''total = 0
def add_to_total(n):
    global total # Ключове слово для глобальний, bad style 
    total = total + n
    return total 

print(add_to_total(5))
print(add_to_total(5))
print(total)'''

'''total = 0
def add_to_total(base_value: int, n: int) -> int:
    return base_value + n # Best style

total = add_to_total(total, 5)
print(total)'''

#Task 1
'''
A perfect number is a number in which the sum of its divisors (excluding itself) are equal to itself.
Write a function that can verify if the given integer n is a perfect number, and return True if it is, or return False if not.
Examples
n = 28 has the following divisors: 1, 2, 4, 7, 14, 28
1 + 2 + 4 + 7 + 14 = 28 therefore 28 is a perfect number, so you should return True
Another example:
n = 25 has the following divisors: 1, 5, 25
1 + 5 = 6 therefore 25 is not a perfect number, so you should return False'''

# num = input ('Input integer number:' )
'''def perfect_number(num: int) -> bool:
    if isinstance(num, int):
        num = int(num)
        sum_div = 0
        for i in range(1, num): 
            if num % i == 0:
                sum_div += i
        return num == sum_div
    else: 
        return 'Bad input'
    

print(perfect_number(25)) 
print(perfect_number(3))
print(perfect_number(28))
print(perfect_number('a'))


def perfect_number(n: int) -> int:
    sum_ = 0
    for i in range(1, n):
        if n % i == 0:
            sum_ += i
    return n == sum_
print(perfect_number(28))'''


'''tuple_example = (1, 2, 3), 4, 5
print(type(tuple_example))'''


## try / except 

import random # дозволяє працювати з псевдорандом
print(random.randint(4, 10)) # Дозволяє повертати в діапозоні числа,  start: end

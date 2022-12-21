'''a = 2
assert a == 4, f'Wrong a value, we wait 4 return {a}'''
'''numbers = [1, 2, 3]
print(numbers)
numbers = numbers + [3] # Добавляємо один елемент 
# Добавляємо один елемент 
print(numbers)

print(numbers)

numbers.append(56) # Добавляємо в кінець один елемент 

numbers.append(1) 
print(numbers)

print(numbers.index(1, 0))
print(numbers.index(1, 1, 6))'''

# Створити два списка, number, square, користувач вводить перший список(з консолі), після цього ми повертаемо квадрат до кожного числа.
# Обгорнути все в функцію з анотацією
# Написати функцію з тестами
# Використати try/except 
# Example: [1,2,3,4,5] -> [1, 4, 9, 16, 25]
'''number = input('Enter some number with comma, e.g. 1,2,3: ')
print(number)
print(type(number))
#Функція підносить до квадрату всі елементи спіска, який вводить користувач
def square(number): 
    number = number.split(',')
    square = [int(num) ** 2 for num in number]
    return square

print(square(number))
def square_assert(): 
    assert square([1,2,3,4,5]) == [1, 4, 9, 16, 25]

square_assert()

try: 
    square(number)
except ValueError: 
    print("Something bad happened!")'''


#assert square([1.2.3]) == [1, 4, 9] f'Error input, you need to use comma ,'''


'''#In this task you will create a function that takes a list of non-negative integers and strings 
# and returns a new list with the strings filtered out.
#Example: 
#filter_list([1,2,'a','b']) == [1,2] 
#filter_list([1,'a','b',0,15]) == [1,0,15] 
#filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def filter_list(lst): 
    filter_lst = []
    for i in lst:
        if isinstance(i, int):
            filter_lst.append(i)
    return filter_lst 

lst = [1,2,'a','b']
print(filter_list(lst))'''

'''numbers = [i for i in range(1, 6)]
# Built-in-function
print(f'Max = {max(numbers)}\nMin = {min(numbers)}\nSum = {sum(numbers)}')

arr = ['new' for _ in range(10)]
print(arr)

squares = [i**2 for i in numbers] # List comprehension, and we can use if 
print(squares)

squares = [i**2 for i in numbers if i % 2] # List comprehension, and we can use if 
print(squares)

squares = [i**2 if i % 2 == 0 else 0 for i in numbers ] # List comprehension, and we can use if 
print(squares)'''

'''str_numbers = ("1.5", "2.3", "5.25")
print(f'String numbers: {str_numbers}')
float_numbers = [float(value) for value in str_numbers]
print(f'Float numbers: {float_numbers}')
print(f'Float numbers sum: {sum(float_numbers)}')'''

'''nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'len(two_by_two): {len(nested_list)}')

for i in nested_list:
    for j in i:
        print(j)
    print('\nNext arr\n')'''

'''# copy of list
first_list = [1, 2, 3]
second_list = first_list[:] # [1, 2, 3]
second_list[0] = 0
print(first_list, second_list)'''

'''def some_function(value, temP_list = []): 

    temP_list.append(value)
    print(temP_list)
    # temP_list.clear()
some_function(3) # Що поверне?
print(some_function.__defaults__) # Звернутись до дефолт значень

# best practice !!! 
def some_function(value, temP_list = None):
    if temP_list is None:
        temP_list = []

    temP_list.append(value)
    print(temP_list)
some_function(3)'''

unsorted_list = [3, 2, 1, 7, 4]
unsorted_list.sort()
print(f'use sort: {unsorted_list}')
numbers = ['twenty', 'one']
numbers.sort(key=len)
print(numbers)

# Task 1
# Створити два списка, number, square, користувач вводить перший список(з консолі), після цього ми повертаемо квадрат до кожного числа.
# Обгорнути все в функцію з анотацією
# Написати функцію з тестами
# Використати try/except
# Example: [1,2,3,4,5] -> [1, 4, 9, 16, 25]

numbers = input('Enter some number with comma, e.g. 1,2,3: ').split(',')


# Функція підносить до квадрату всі елементи спіска, який вводить користувач
def square_numbers(numbers: list) -> list:
    try:
        return [float(x) ** 2 for x in numbers]
    except (ValueError, SyntaxError):
        return "You need to use only number"


print(square_numbers(['a', ':']))


def test_square_arr():
    assert square_numbers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
    assert square_numbers([1.5, 2, 3, 4]) == [2.25, 4, 9, 16]
    assert square_numbers(['a', 1]) == "You need to use only number"
    assert square_numbers([]) == []
    assert square_numbers([--1, -1, -1]) == [1, 1, 1]


print(test_square_arr())


# Practice block 1
# 1. Write a program to compute the difference beyween two list.

def compute_difference(first: list, second: list) -> tuple:
    lst1 = [i for i in first if i not in second]
    lst2 = [i for i in second if i not in first]
    return (lst1, lst2)


def test_compute_difference():
    result1 = compute_difference(['a', 'b', 'c', 'd'], ['c', 'd', 'e'])
    assert result1 == (['a', 'b'], ['e'])

    result2 = compute_difference([], ['c', 'd', 'e'])
    assert result2 == ([], ['c', 'd', 'e'])

    result3 = compute_difference([1, 2, 3], [4, 5, 6])
    assert result3 == ([1, 2, 3], [4, 5, 6])

    result4 = compute_difference([1, 2, 3], [2, 3, 4])
    assert result4 == ([1], [4])


print(test_compute_difference())


# 2. Given an array of integers nums and an integer target, return indeces of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return answer in any order.

def sum_of_two(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(len(nums)):
            sum_nums = nums[i] + nums[j]
            if (i != j) and (sum_nums == target):
                return [i, j]


def test_sum_of_two():
    result1 = sum_of_two([2, 7, 11, 15], 9)
    assert result1 == [0, 1]

    result2 = sum_of_two([3, 2, 4], 6)
    assert result2 == [1, 2]

    result3 = sum_of_two([3, 3], 6)
    assert result3 == [0, 1]


print(test_sum_of_two())


# 3. Optional (hard): Longest Increasing Sequence
'''Have the function longest_increasing_sequence take the list of positive integers and return
the length of the longest increasing subsequense (LIS). A LIS is a subset of the original list where the numbers
are in sorted order, from lowest to highest, and are in increasing order. The sequence does nit need to be contiguous or unique,
and there can be several different subsequences. For example: if arr is [4, 3, 5, 1, 6] then a possible LIS is [3, 5, 6]
and another is [1, 6]. For this input, you program should return 3 because that is the length of the longest increasing subsequence. '''


def longest_increasing_sequence(arr: list) -> int:
    m = len(arr)
    set_subset = []
    for i in range(m):
        subset = [arr[i]]  # create subset with the first element in given arr
        for j in range(i+1, m):  # проходимо по всім наступним елементам списку
            if subset[-1] < arr[j]:  # якщо наступний елемент більше за попередній елемент у створеному subset, додаємо його
                subset.append(arr[j])
        set_subset.append(subset)  # create sequence of all increasing subsets
    len_subset = []
    for set in set_subset:
        len_subset.append(len(set))  # create list with length of all subset
    return max(len_subset)  # find max length


def test_longest_increasing_sequence():
    result1 = longest_increasing_sequence([9, 9, 4, 2])
    assert result1 == 1

    result2 = longest_increasing_sequence([10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90])
    assert result2 == 7

    result3 = longest_increasing_sequence([4, 3, 5, 1, 6])
    assert result3 == 3


print(test_longest_increasing_sequence())


# Practice block 2

# 1. Create a list with next values [1, 4, 2, 5]. Create a sorted copy of that list w/o changing the original list
lst = [1, 4, 2, 5]
lst_sort = sorted(lst)
print(lst, lst_sort)
print(lst == lst_sort)


# 2. Sort the following list by population. Calcilate average and total population for cities from this list

population = [
        ('New York City', 8550405),
        ('Los Angeles', 3792621),
        ('Chicago', 2695598),
        ('Houston', 2100263),
        ('Philadelphia', 1526006),
        ('Phoenix', 1445632),
        ('San Antonio', 1327407),
        ('San Diego', 1307402),
        ('Dallas', 1197816),
        ('San Jose', 945942),
]


def sort_order():
    for city in population:
        return city[1]


population.sort(key=lambda x: x[1])
print(population)


def stat_population():
    total_population = 0
    for city in population:
        total_population += city[1]
    avg_population = total_population / len(population)
    return f'Average populationtotal = {avg_population:.2f}, and total population = {total_population}'


print(stat_population())

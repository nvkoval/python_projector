# Practice block 1:
# 1. Create an outer function that will accept two parameters, a and b
def outer_func(a, b):
    return a, b


print(outer_func(5, 3))


# 2. Create an inner function inside an outer function that will calculate the addition of a and b
def outer_func(a, b):
    def inner_func():
        return a + b
    return inner_func()


print(outer_func(1, 2))


# 3. At last, an outer function will add 5 into addition and return it
def outer_func():
    a = int(input('Input a = '))
    b = int(input('Input b = '))

    def inner_func():
        return a + b
    return inner_func() + 5


# Practice block 2
# 1. Write a program that asks user to enter an integer and convert it to int.
# If the user enters something that is not an integer, program should catch an error and ask the user to enter an integer again.
# if user inputs an integer, program should print this number and quit w/o any error.
def convert_to_int():
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        number = int(input("Enter an integer again: "))
    return number


# 2. Write a program that asks the user to input a string and an integer n.
# Then display the character at index n in the string.
# You should handle an error properly and display proper error message.
def char_in_string():
    try:
        string = input('Enter a string: ')
        idx = int(input("Enter an integer n = "))
        return (string[idx])
    except ValueError as e:
        return f'That n was not an integer: {e}'
    except IndexError as i:
        return f'Something went wrong: {i}'


# Practice block 3:
# 1. Write a function that simulate a dice roll and returns the result from 1 to 6.
import random


def dice_roll():
    return random.randint(1, 6)


# 2. Write a function that simulate 10_000 rolls and returns the number of times that the dice roll for each value
def dice_roll_10_000():
    dice_roll_1 = 0
    dice_roll_2 = 0
    dice_roll_3 = 0
    dice_roll_4 = 0
    dice_roll_5 = 0
    dice_roll_6 = 0
    for i in range(10_000):
        dice_roll = random.randint(1, 6)
        match dice_roll:
            case 1:
                dice_roll_1 += 1
            case 2:
                dice_roll_2 += 1
            case 3:
                dice_roll_3 += 1
            case 4:
                dice_roll_4 += 1
            case 5:
                dice_roll_5 += 1
            case 6:
                dice_roll_6 += 1
    return f'number of times that the dice roll for each value: \n1: {dice_roll_1 },\
        \n2: {dice_roll_2},\
        \n3: {dice_roll_3},\
        \n4: {dice_roll_4},\
        \n5: {dice_roll_5},\
        \n6: {dice_roll_6},\
        '


# list with number
def dice_roll_10_000():
    number_dice_roll = [0] * 6
    for i in range(10_000):
        dice_roll = random.randint(1, 6)
        number_dice_roll[dice_roll - 1] += 1
    return f'number of times that the dice roll for each value: {number_dice_roll}'


# with dictionary
def dice_roll_10_000():
    number_dice_roll = {}
    for i in range(10_000):
        dice_roll = random.randint(1, 6)
        if dice_roll not in number_dice_roll.keys():
            number_dice_roll[dice_roll] = 1
        else:
            number_dice_roll[dice_roll] += 1
    return number_dice_roll


# with defoult_dict
from collections import defaultdict


def dice_roll_10_000():
    number_dice_roll = defaultdict(int)
    for i in range(10_000):
        dice_roll = random.randint(1, 6)
        number_dice_roll[dice_roll] += 1
    return number_dice_roll


# 3. Simulate an election for two candidates.
# Program should take amount of regions and rating for 1st candidate in each region (in percentage).
# Program should run election in every region. In every region, program should ask 10 000 voters.
# Candidate count as a winner if he gains more than 50% of all votes.
# Program should print the result of the election for each region and the winner
'''Example:

Enter number of regions: 2
Enter rating for 1st candidate in each region: 34, 56

Region 1: 3456 votes for 1st candidate, 6544 votes for 2nd candidate
Region 2: 5623 votes for 1st candidate, 4356 votes for 2nd candidate
Result: 2nd candidate won with 10900 votes and 54.5% of all votes'''


def election():
    num_region = int(input('Enter number of regions: '))
    rating = input('Enter rating for 1st candidate in each region with comma separation: ')
    rating_num = [int(x.strip()) for x in rating.split(',')]  # перетворюємо строку у список

    def region_election(rating):
        cand_1 = 0
        for i in range(10_000):
            if random.randint(0, 100) < rating:
                cand_1 += 1
        return cand_1

    cand_1_all = 0
    cand_2_all = 0

    for i in range(num_region):
        # рахуємо кількість голосів за кожного з кандидатів у кожному регіоні
        cand_1 = region_election(rating_num[i])
        cand_2 = 10_000 - cand_1
        print(f'Region {i+1}: {cand_1} votes for 1st candidate, {cand_2} votes for 2nd candidate')

        # сумарна кількість голосів за кожного з кандидатів
        cand_1_all += cand_1
        cand_2_all += cand_2

    # результати голосування у відсотках
    cand_1_all_percent = cand_1_all / (10_000 * num_region) * 100
    cand_2_all_percent = cand_2_all / (10_000 * num_region) * 100

    # оголошення переможця
    if cand_1_all_percent > 50:
        result = f'Result: 1nd candidate won with {cand_1_all} votes and {cand_1_all_percent:.2f}% of all votes'
    elif cand_2_all_percent > 50:
        result = f'Result: 2nd candidate won with {cand_2_all} votes and {cand_2_all_percent:.2f}% of all votes'
    return result


print(election())


# Practice block 4
# 1. Create a tuple with your first name, last name, and age.
my_tuple = ('Nataia', 'Koval', 41)
print(my_tuple)

# 2. Print your last name using indexing.
print(my_tuple[1])

# 3. Create three variables in one line that extracted from tuple that you created in step 1.
first_name, last_name, age = my_tuple
print(first_name, last_name, age)

# 4. Print your name letter by letter from this tuple
for name in my_tuple[:-1]:
    for letter in name:
        print(letter)

# 5. Create a new tuple that contains all info from the first tuple but remove first letter from all strings
new_tuple = (first_name[1:], last_name[1:], age)
print(new_tuple)

# 6. Create a tuple with two values. First one is (1, 2), second one is (3, 4).
tuple_two = ((1, 2), (3, 4))
print(tuple_two)


# 7. Create a program that calculates the sum of all values in the tuple and print it to the console.
def sum_tuple(tpl):
    sum_tuple = 0
    for element in tpl:
        sum_tuple += sum(element)
    return sum_tuple


print(sum_tuple(tuple_two))

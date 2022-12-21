# Task 1. Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
# Input: low = 3, high = 7 Output: 3 Explanation: The odd numbers between 3 and 7 are [3,5,7]. Example 2:
# Input: low = 8, high = 10 Output: 1 Explanation: The odd numbers between 8 and 10 are [9].

low = 8
hight = 10


def count_odd(low, hight):
    return len([i for i in range(low, hight + 1) if i % 2 != 0])


count_odd(low, hight)


def count_odd_1(low, hight):
    if low % 2 == 0:
        return len(range(low + 1, hight + 1, 2))
    else:
        return len(range(low, hight + 1, 2))


count_odd_1(low, hight)


# Task 2. You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary.
# Input: salary = [4000,3000,1000,2000] Output: 2500.00000
# Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively. Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500 Example 2:
# Input: salary = [1000,2000,3000] Output: 2000.00000
# Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively. Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

salary = [4000, 3000, 1000, 2000]


def avg_without_max_min(salary):
    salary_without_max_min = sorted(salary)[1:-1]
    return sum(salary_without_max_min) / len(salary_without_max_min)


print(avg_without_max_min(salary))


# Task 3
# In an array of integers of length n + 1 (n > 1), every number in the range 1...n appears once
# except for one number which appears twice (so the array’s length is n+1).
# Write an efficient function that finds the number that appears twice.
# 1,2,2,3 => 2 1,2,3,3 => 3 2,1,4,3,5,4 => 4


def appears_twice(arr: list) -> int:
    return sum(arr) - sum(set(arr))


print(appears_twice([1, 2, 2, 3]))
print(appears_twice([1, 2, 3, 3]))
print(appears_twice([2, 1, 4, 3, 5, 4]))


def appears_twice_2(arr: list) -> int:
    for i in set(arr):
        if arr.count(i) == 2:
            return i


print(appears_twice_2([1, 2, 2, 3]))
print(appears_twice_2([1, 2, 3, 3]))
print(appears_twice_2([2, 1, 4, 3, 5, 4]))


# Task 4 Intersection
# Given two arrays of numbers where each one contains unique values and is already sorted in ascending order,
# find the number of elements that belong to both arrays.

arr_1 = [1, 2, 3]
arr_2 = [2, 3, 5]


def elements_belong_to_both_arrays(arr_1: list, arr_2: list) -> int:
    return len(set(arr_1).intersection(set(arr_2)))


print(elements_belong_to_both_arrays(arr_1, arr_2))


# Task 5. RLE
# Given a string of letters (without numbers), create a string encoding it by the rules where the first character is char itself,
# followed by a number indicating the number of letter repeats.
# Examples:
# ABBA => A1B2A1 ATTTGC => A1T3G1C1


def letter_repeat(str: str) -> str:
    str_new = ''
    count_char = 1
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            count_char += 1
        else:
            str_new = f'{str_new}{str[i]}{count_char}'
            count_char = 1
    str_new = f'{str_new}{str[-1]}{count_char}'
    return str_new


# Practice 1:
# 1. Create emtpy dictionary named en_ua_dictionary.

en_ua_dictionary = {}
print(en_ua_dictionary, type(en_ua_dictionary))


# 2. Add few key-value pairs to the dictionary. Example: 'red': 'червоний'
en_ua_dictionary['red'] = 'червоний'
en_ua_dictionary['blue'] = 'блакитний'
en_ua_dictionary['yellow'] = 'жовтий'


# 3. Check if the dictionary contains key 'blue' and 'purple'. If not, set their values to unknown.
print(en_ua_dictionary.setdefault('blue', 'unknown'))
print(en_ua_dictionary.setdefault('purple', 'unknown'))

print(en_ua_dictionary)


# 4. Create a loop over existing values and print them to the console in the following format:
# Red in Ukrainian is червоний

for key, value in en_ua_dictionary.items():
    print(f'{key.title()} in Ukrainian is {value}')


# 5. Delete all key-values pairs from the dictionary if the lenght of value is lower than 5.

keys_lower_5 = [key for key, value in en_ua_dictionary.items() if len(value) > 5]
for key in keys_lower_5:
    en_ua_dictionary.pop(key, None)


print(en_ua_dictionary)


# 6. Write a game where user should guess of a capital of the country that you have in your dictionary.
# capitals = { 'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Rome',
# 'USA': 'Washington', 'Canada': 'Ottawa', 'Switzerland': 'Bern', 'Austria': 'Vienna',
# 'Belgium': 'Brussels', 'Sweden': 'Stockholm', 'Norway': 'Oslo', 'Denmark': 'Copenhagen',
# 'Finland': 'Helsinki', 'Poland': 'Warsaw', 'Romania': 'Bucharest', 'Bulgaria': 'Sofia',
# 'Greece': 'Athens', ... }
# You should show user a random country from the list and ask him to guess the capital.
# If user input right capital, print "You are right!", add him a point and ask him to guess another country.
# If not, you should ask again.
# User should be able to quit the game by typing "exit".
# You should print current score after each round. Also, you should print the final score before user quit the game.

import random

capitals = {'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Rome',
            'USA': 'Washington', 'Canada': 'Ottawa', 'Switzerland': 'Bern', 'Austria': 'Vienna',
            'Belgium': 'Brussels', 'Sweden': 'Stockholm', 'Norway': 'Oslo',
            'Denmark': 'Copenhagen', 'Finland': 'Helsinki', 'Poland': 'Warsaw',
            'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens', }


def capital_game(country='', scores=0):
    # Choose a random country
    if country == '':
        country = random.choice(list(capitals.keys()))

    print(f'What is the capital of {country}?')
    answer = input('Enter Your answer: ')

    # Check the correctness of the answer
    if answer == capitals[country]:
        print('You are right!')
        scores += 1
        print(f'Yor scores = {scores}')
        capitals.pop(country)  # If the answer is correct, delete this country from dictionary
        print(len(capitals))
        if len(capitals) != 0:
            capital_game(scores=scores)  # If user input right capital ask him to guess another country
        else:
            print(f'The game is over. Your final scores = {scores}')  # If user guess all country from the dictionary, the game is over
    elif answer == 'exit':  # Quit the game by typing "exit"
        print(f'The game is over. Your final scores = {scores}')
    elif answer != capitals[country]:  # If user input wrong capital ask again
        print('You are wrong! Try again')
        capital_game(country=country, scores=scores)


capital_game()


# Optional:
# Give user a hint if he guesses wrong. Hint should looks like first letter of the capital.
# If you user make another mistake, you should print one more letter from the capital.
# If user make a mistake you should decrement his lives. Initial amount of lives is 3. Game will end when user has no lives left.
# You should print the final score after user has no lives left.

capitals = {'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Rome',
            'USA': 'Washington', 'Canada': 'Ottawa', 'Switzerland': 'Bern', 'Austria': 'Vienna',
            'Belgium': 'Brussels', 'Sweden': 'Stockholm', 'Norway': 'Oslo',
            'Denmark': 'Copenhagen', 'Finland': 'Helsinki', 'Poland': 'Warsaw',
            'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens', }


def capital_game(country='', scores=0, count_error=0, lives=3):
    # Choose a random country
    if country == '':
        country = random.choice(list(capitals.keys()))
    print(f'What is the capital of {country}?')
    answer = input('Enter Your answer: ')

    # Check the correctness of the answer
    if answer == capitals[country]:
        print('You are right!')
        scores += 1
        print(f'Yor scores = {scores}')
        capitals.pop(country)  # If the answer is correct, delete this country from dictionary
        if len(capitals) != 0:
            capital_game(scores=scores, lives=lives)  # If user input right capital ask him to guess another country
        else:
            print(f'The game is over. Your final scores = {scores}')  # If user guess all country from the dictionary, the game is over
    elif answer == 'exit':  # Quit the game by typing "exit"
        print(f'The game is over. Your final scores = {scores}')
    elif answer != capitals[country]:  # If user input wrong capital ask again
        print('You are wrong!')
        if lives > 0:
            print(f'Try again. The first letters of the capital is "{capitals[country][:count_error+1]}"')  # Give a hint
            count_error += 1
            lives -= 1  # Decrement lives if user make a mistake
            capital_game(country=country, scores=scores, count_error=count_error, lives=lives)
        else:
            print(f'The game is over. Your final scores = {scores}')  # Game is end when user has no lives left


capital_game()


# Optional
'''Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

* I can be placed before V (5) and X (10) to make 4 and 9.
* X can be placed before L (50) and C (100) to make 40 and 90.
* can be placed before D (500) and M (1000) to make 400 and 900.
'''
# 1. Given a roman numeral, convert it to an integer.
'''Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

'''Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''


def roman_to_int(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    if (1 <= len(s) <= 15) and all(char in 'IVXLCDM' for char in s):
        while len(s) > 1:
            if roman_dict[s[0]] < roman_dict[s[1]]:
                num += roman_dict[s[1]] - roman_dict[s[0]]
                s = s[2:]
            elif roman_dict[s[0]] == roman_dict[s[1]]:
                num += roman_dict[s[0]] + roman_dict[s[1]]
                s = s[2:]
            else:
                num += roman_dict[s[0]]
                s = s[1:]
        if len(s) > 2 and s[-3] == s[-2] == s[-1]:
            num += roman_dict[s[-1]]
        elif len(s) == 1:
            num += roman_dict[s[0]]
        return num
    return 'Bad input'


def test_roman_to_int():
    result1 = roman_to_int("III")
    assert result1 == 3

    result1 = roman_to_int("LVIII")
    assert result1 == 58

    result1 = roman_to_int("MCMXCIV")
    assert result1 == 1994


test_roman_to_int()


# Optional
# 2. Try to create a function that will do reverse operation - from integer to roman
def int_to_roman(num: int) -> str:
    roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    rom_num = ''
    if num in range(1, 4000):
        for i in range(len(str(num))-1, -1, -1):
            digit = num // 10**i
            num_ = digit * 10**i  # Розкладаємо число на доданки по степеням числа 10
            if num_ in roman_dict.keys():
                rom_num += roman_dict[num_]
            elif digit == 0:
                rom_num = rom_num
            elif digit < 4:
                rom_num += digit * roman_dict[num_ / digit]
            elif digit > 5:
                rom_num += roman_dict[5*10**i] + (digit - 5) * roman_dict[num_ / (digit)]
            num -= num_
        return rom_num
    return 'Bad input'


def test_int_to_roman():
    result1 = int_to_roman(3)
    assert result1 == "III"

    result1 = int_to_roman(58)
    assert result1 == "LVIII"

    result1 = int_to_roman(1994)
    assert result1 == "MCMXCIV"

    result1 = int_to_roman(20)
    assert result1 == "XX"


# Optional
# 3. Write an algorithm to determine if a number n is happy.
'''A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true

Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:

Input: n = 2
Output: false

Constraints:

1 <= n <= 231 - 1
'''


def is_happy(n: int) -> bool:
    def sum_square(n: int) -> int:
        return sum([int(i)**2 for i in str(n)])

    result = []
    while n not in result:
        result.append(n)
        n = sum_square(n)
    return (1 in result)


def test_is_happy():
    result1 = is_happy(19)
    assert result1 is True

    result2 = is_happy(2)
    assert result2 is False

    result3 = is_happy(524)
    assert result3 is False


# 3. Given a string s, find the length of the longest substring without repeating characters.

'''Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''


def length_of_longest_substring(s: str) -> int:
    dict_substring = {}
    substring = ''
    for char in s:
        substring = substring[substring.find(char)+1:]
        substring += char
        dict_substring[substring] = len(substring)
    return max(dict_substring.items(), key=lambda x: x[1])[1] if len(s) > 0 else 0


def test_length_of_longest_substring():
    result1 = length_of_longest_substring('abcabcabc')
    assert result1 == 3

    result2 = length_of_longest_substring('bbbbb')
    assert result2 == 1

    result3 = length_of_longest_substring("pwwkew")
    assert result3 == 3

    result4 = length_of_longest_substring("")
    assert result4 == 0

    result5 = length_of_longest_substring(" ")
    assert result5 == 1

    result6 = length_of_longest_substring("p")
    assert result6 == 1


def length_of_longest_substring_2(s: str) -> int:
    dict_substring = {}
    # Create all possible substring
    for i in range(len(s)):
        substring = ''
        while s[i] not in substring:
            substring += s[i]
            if i < len(s) - 1:
                i += 1
        dict_substring[substring] = len(substring)
    return max(dict_substring.items(), key=lambda x: x[1])[1] if len(s) > 0 else 0

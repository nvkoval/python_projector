# Task 1. Вводятся целые числа. Необходимо четные добавлять в начало списка, а нечетные - в конец.
def even_odd_list(nums: list[int]) -> list:
    return sorted([num for num in nums if num % 2 == 0]) + sorted([num for num in nums if num % 2 != 0])


def test_even_odd_list():
    assert even_odd_list([1, 12, 3, 2, 5, 8]) == [2, 8, 12, 1, 3, 5]

    assert even_odd_list([]) == []

    assert even_odd_list([13, 7, 5]) == [5, 7, 13]


test_even_odd_list()


# Task 2. Вводится строка. Необходимо определить в ней проценты прописных(больших) и строчных (малых) букв.
def upper_lower_percent(s: str) -> float:
    all_letter = len([x for x in s if x.isalpha()])
    upper_letter_percent = len([x for x in s if x.isupper()]) / all_letter * 100
    lower_letter_percent = 100 - upper_letter_percent
    return f'Upper letter: {upper_letter_percent:.2f}%, lower letter: {lower_letter_percent:.2f}%'


print(upper_lower_percent('RgejY k:3'))

# Task 3. Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# Example:
# Input: nums = [1,3,5,6], target = 5 Output: 2
# Input: nums = [1,3,5,6], target = 2 Output: 1
# Input: nums = [1,3,5,6], target = 7 Output: 4


def index_target(nums: list[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        return sorted(nums).index(target)


def test_index_target():
    assert index_target([1, 3, 5, 6], 5) == 2

    assert index_target([1, 3, 5, 6], 2) == 1

    assert index_target([1, 3, 5, 6], 7) == 4


test_index_target()

# Task 4. Write an efficient function that checks whether any permutation of an input string is a palindrome. Note that the function is not a palindrome check.
'''Examples:
"civic" should return True
"ivicc" should return True (because “civic” is a permutation of “ivicc”)
"civil" should return False
"livci" should return False
'''


# If we have two input string
def permutation_is_palindrome(str1: str, str2: str) -> bool:
    return str1 == str1[::-1] and sorted(str1) == sorted(str2)


def test_permutation_is_palindrome():
    assert permutation_is_palindrome("civic", "ivicc") is True

    assert permutation_is_palindrome("civic", "civil") is False

    assert permutation_is_palindrome("civic", "livci") is False

    assert permutation_is_palindrome("anna", "nana") is True


# If we have one input string
from collections import defaultdict


def permutation_is_palindrome_one(s: str) -> bool:
    count_letter = defaultdict(int)
    for letter in s:
        count_letter[letter] += 1
    odd_count_letter = len([x for x in list(count_letter.values()) if x % 2 != 0])
    return odd_count_letter == 1 or odd_count_letter == 0


def test_permutation_is_palindrome():
    assert permutation_is_palindrome_one("civic") is True

    assert permutation_is_palindrome_one("ivicc") is True

    assert permutation_is_palindrome_one("civil") is False

    assert permutation_is_palindrome_one("livci") is False

    assert permutation_is_palindrome_one("anna") is True


test_permutation_is_palindrome()

# You have 100 cats.
'''
One day you decide to arrange all your cats in a giant circle.
Initially, none of your cats have any hats on. You walk around the circle 100 times,
always starting at the same spot, with the first cat (cat # 1).
Every time you stop at a cat, you either put a hat on it if it doesn’t have one on,
or you take its hat off if it has one on.

The first round, you stop at every cat, placing a hat on each one.
The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
Write a program that simply outputs which cats have hats at the end.

Optional: Make function that can calculate hat with any amount of rounds and cats.

Here you should write an algorithm, after that, try to make pseudo code. Only after that start to work. Code is simple here, but you might struggle with algorithm.
Therefore don`t try to write a code from the first attempt.'''


'''
7 cats                                                   [0, 0, 0, 0, 0, 0, 0]
1 round: every cats with hats                            [1, 1, 1, 1, 1, 1, 1]
2 round: every second cat change wit hat / without hat   [1, 0, 1, 0, 1, 0, 1]
3 round: every third cat change wit hat / without hat    [1, 0, 0, 0, 1, 1, 1]
4 round: every 4th cat change wit hat / without hat      [1, 0, 0, 1, 1, 1, 1]
5 round: every 5th cat change wit hat / without hat      [1, 0, 0, 1, 0, 1, 1]
6 round: every 6th cat change wit hat / without hat      [1, 0, 0, 1, 0, 0, 1]
7 round: every 7th cat change wit hat / without hat      [1, 0, 0, 1, 0, 0, 0]

initial list with 100 elements = 0
For loop in range(cats = 100):
    on every i step we change all i-th elements from list to opposite (0 -> 1, 1 -> 0)
print index of all elements which == 1
'''


def cats_hats(cats: int) -> list:
    hats = [0] * cats
    for i in range(1, cats + 1):
        hats = [not x if idx % i == 0 else x for idx, x in enumerate(hats, start=1)]
    return [idx for idx, x in enumerate(hats, start=1) if x == 1]


print(cats_hats(100))
print(cats_hats(7))

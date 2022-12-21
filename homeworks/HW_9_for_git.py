# Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.


# The first solution
def single_number_1(nums: list[int]) -> int:
    for num in set(nums):
        if nums.count(num) == 1:
            return num


# The second solution
def single_number_2(nums: list[int]) -> int:
    return sum([num*2 for num in set(nums)]) - sum(nums)


# Test the correctness of code
def test_single_number():
    assert single_number_1([2, 2, 1]) == 1
    assert single_number_2([2, 2, 1]) == 1

    assert single_number_1([4, 1, 2, 1, 2]) == 4
    assert single_number_2([4, 1, 2, 1, 2]) == 4

    assert single_number_1([1]) == 1
    assert single_number_2([1]) == 1


# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# The first solution
def is_anagram_1(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


# The second solution
def is_anagram_2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True


# Test the correctness of code
def test_is_anagram():
    assert is_anagram_1("anagram", "nagaram") is True
    assert is_anagram_2("anagram", "nagaram") is True

    assert is_anagram_1("rat", "car") is False
    assert is_anagram_2("rat", "car") is False


# Third Maximum Number
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number


# The first solution
def third_max_1(nums: list[int]) -> int:
    if len(set(nums)) > 2:
        return sorted(set(nums))[-3]
    else:
        return max(nums)


# The second solution
def third_max_2(nums: list[int]) -> int:
    nums = set(nums)
    if len(set(nums)) > 2:
        for i in range(3):
            third_max = max(nums)
            nums.remove(third_max)
        return third_max
    return max(nums)


# Test the correctness of code
def test_third_max():
    assert third_max_1([3, 2, 1]) == 1
    assert third_max_2([3, 2, 1]) == 1

    assert third_max_1([1, 2]) == 2
    assert third_max_2([1, 2]) == 2

    assert third_max_1([2, 2, 3, 1]) == 1
    assert third_max_2([2, 2, 3, 1]) == 1

nums = [1, 1, 1, 1, 1]
#print(nums[:4], nums[5:])

'''def remove_duplicates(nums: list[int]) -> int: 
    i = 0
    while len(nums[i:]) != 0:
        while len(nums[i:])>1 and nums[i] == nums[i+1]:
            nums.pop(i)
            print(nums)
        i += 1
    return len(nums)

remove_duplicates([1, 1, 1, 1, 1])'''

for idx, val in enumerate(nums):
    while nums[idx] == nums[idx+1]:
        nums.pop(idx)
    print(nums)
    
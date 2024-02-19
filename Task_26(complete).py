"""
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.
"""

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

if len(nums) == 0:
    print(0)
slow = 0
for fast in range(1, len(nums)):
    if nums[slow] != nums[fast]:
        slow += 1
        nums[slow] = nums[fast]
print((nums[:slow+1]))

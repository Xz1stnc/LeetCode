def find_max_consecutive_ones(nums: list[int]) -> int:
    counter = 0
    maxi = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            if counter == maxi:
                counter += 1
                maxi += 1
            else:
                counter += 1
        else:
            counter = 0
    return maxi


count = find_max_consecutive_ones([1, 1, 0, 1, 1, 1, 1, 0, 1])
print(count)

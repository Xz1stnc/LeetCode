def shuffle(nums: list[int], n: int) -> list[int]:
    arr1 = nums[0: n]
    arr2 = nums[n:]
    target = []
    for i in range(0, n):
        target.append(arr1[i])
        target.append(arr2[i])
    print(target)

shuffle([2, 5, 1, 3, 4, 7], 3)

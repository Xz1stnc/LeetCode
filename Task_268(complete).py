def missingnumber(nums: list[int]) -> int:
    correct_list = set([i+1 for i in range(-1, len(nums))])
    n = list(correct_list.difference(set(nums)))
    return n[0]


a = missingnumber([1, 0])
print(a)

def max_values(nums):
    nums.sort()
    return(nums[-1])



print(max_values([4, 7, 2, 8, 10, 9])) # -> [4, 5]
# print(max_values([-5, -2, -1, -11])) # -> [1, 2]
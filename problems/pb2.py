def max_values(nums):
    # result = [nums.index(i) for i in sorted(nums, reverse=True)][:2]
    # return(result)

 result = [nums.index(i) for i in sorted(nums, reverse=True)][:2]
 return(result)



# print(max_values([4, 7, 2, 8, 10, 9])) # -> [4, 5]
# print(max_values([-5, -2, -1, -11])) # -> [1, 2]
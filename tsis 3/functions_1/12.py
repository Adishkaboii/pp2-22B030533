def histogram(nums):
    for i in range(0,len(nums)):
        for j in range(0,nums[i]):
             print('*', end = ' ')
        print()
nums = [int(x) for x in input().split()]
histogram(nums)

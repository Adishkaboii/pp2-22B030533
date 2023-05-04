def has_007(nums):
    for i in range(0,len(nums)-2):
        if(nums[i]==0 and nums[i+1]==0 and nums[i+2]==7):
           return True
     
    return False

num_list = [int(x) for x in input().split()]

print(has_007(num_list))

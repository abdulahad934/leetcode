def toSum(nums, target):
    
    for i in range(len(nums)):
       
        for j in range(len(nums)):
            if nums[i] - nums[j] == target:
                return [j, i]
        

    



nums = [2, 1, 2, 3, 4,  10, 20, 30, 49, 4, 5]

target = 20
toSum(nums, target)

print(toSum(nums, target))
# def age_Checar(age, clas):
#     if age >= 18  : 
#         return "Adult"
#     else:
#         return "Child"
       
    
    
# age = int(input("Enter Age : "))


# print(age_Checar(age))



# def evenOddd_checur(nums):
    
#     even =[x for x in nums if x % 2 ==0 ]
    
#     odd = [x for x in nums if x%2 != 0]
    
#     result = even + odd
    
#     print(result)


# nums = [1, 2, 3, 4, 5, 6, 7]

# evenOddd_checur(nums)


# def addToNumber(nums1, nums2):
    
    
#     nums1 = [x for x in nums1]
#     nums2 = [x for x in nums2]
    
#     result = sum(nums1 + nums2)
#     print(result)
    
    
    
    
    
    
    
    
    
    
    
# nums1 = [1,2,3,4,5,6]

# nums2 = [7,8, 9, 10, 11]

# addToNumber(nums1, nums2)
        
        

# def list_Add(nums1, nums2):
    
#     index = 3
    
#     nums1[1: 4]
#     print(nums1[0:4])
    
    
#     result = nums1[index] + nums2[index]
#     print(result)
        
    
    # result = [nums1[i] + nums2[i] for i in range(min(len(nums1), len(nums2)))]
    # print(result)
    # result = []
    
    # for i in range(min(len(nums1), len(nums2))):
    #     value = nums1[i] + nums2[i]
    #     result.append(value)
    # print(result)
        
            
            
            


# nums1 = [1, 2, 3, 4, 5, 6]
# nums2 = [7, 8, 9, 10, 11, 12]

# list_Add(nums1, nums2)
            
        
        



def list_operation(nums, target):
    
    x = [2, 2, 3, 4, 5, 6, 7, 19]
    nums.ap
    print([len(nums)//2 ])
    
    squares = [z**2 for z in nums]
    print(squares)
    
    
    # diff = 0
    # seen = {}
    
    # for i, nums in enumerate(nums):
    #     diff = target - i
        
    #     if diff in seen:
    #         return[seen[diff], i]
        
    #     seen[nums] = i
    
    # return 0
        






nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10

list_operation(nums, target)

print(list_operation(nums, target))
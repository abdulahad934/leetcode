def addToNumbers(L1, L2):
     
   L1 = int("".join(str(i) for i in L1))
   L1 = int("".join(i for i in str(L1)[:: -1]))
   
   L2 = int("".join(str(i) for i in L2))
   L2 = int("".join(i for i in str(L2)[:: -1]))
   
   
   
   result = L1 + L2
   
   result = int(str(result)[::-1])
   return result
    
    
    
    
    
    
    
    
    


L1 = [2, 4, 3]

L2 = [5, 6, 4]

print(addToNumbers(L1, L2))
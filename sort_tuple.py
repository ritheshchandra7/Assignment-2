# Function to sort the list of tuples by its second item
def Sort_Tuple(tup): 
    list1 = len(tup) 
    for i in range(0, list1): 
           
        for j in range(0, list1-i-1): 
            if (tup[j][-1] > tup[j + 1][-1]): 
                temp = tup[j] 
                tup[j]= tup[j + 1] 
                tup[j + 1]= temp 
    return tup 
    
tup =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
         
print(Sort_Tuple(tup))
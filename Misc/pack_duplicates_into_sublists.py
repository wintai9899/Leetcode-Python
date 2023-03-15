import itertools

def packDuplicates(nums):
    res= [] 
    
    for num,group in itertools.groupby(nums):
        res.append(list(group))
    
    return res
    
    
print(packDuplicates([1,2,2,2,3,3,4,5,5,5,5,6]))    
# [1,2,2,2,3,3,4,5,5,5,5,6] -> [[1],[2,2,2,],[3,3],[4],[5,5,5,5],[6]]

def permutationString(s):
    output = ""
    def permute(nums):
        
        if len(nums) == 1:
            return [nums.copy()]
        res = [] 

        for _ in range(len(nums)):
            leftOut = nums.pop(0)
            perms = permute(nums)

            for perm in perms:
                perm.append(leftOut)

            res.extend(perms)
            nums.append(leftOut)
        
        return res

    output = permute(list(s))
    result = []
    for permutations in output:
        tempStr = "".join(permutations)
        result.append(tempStr)
    
    return result
    

    # XYZ”, “YXZ”, “ZYX”, “XZY”, “YZX”, “ZXY”.
print(permutationString("XYZ"))
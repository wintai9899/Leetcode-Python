#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base case 
        if len(nums) == 1:
            return [nums.copy()]

        for _ in range(len(nums)):
            # [1,2,3] -> [2,3]
            leftOut = nums.pop(0)
            #[[2,3],[3,2]]
            perms = self.permute(nums)

             #[[2,3],[3,2]] -> [[2,3,1],[3,2,1]]
            for perm in perms:
                perm.append(leftOut)
            
            # add to result 
            res.extend(perms)
            # put back to nums
            nums.append(leftOut)

        return res


        
# @lc code=end

        
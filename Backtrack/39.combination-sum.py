#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        
        def backtrack(i, curSum, curList):
            if i == len(candidates) or curSum > target:
                return
            
            if curSum == target:
                res.append(curList.copy())
                return 
            # decision to include candidate
            curList.append(candidates[i])
            backtrack(i, curSum + candidates[i], curList)
            # decision not to include 
            curList.pop()
            backtrack(i + 1, curSum, curList)
            
        backtrack(0,0,[])
        
        return res
            
            
        
# @lc code=end


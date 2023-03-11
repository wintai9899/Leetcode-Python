#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(i, curList, curSum):
            if i == len(candidates) or curSum > target:
                return 

            # found match sum 
            if curSum == target:
                res.append(curList.copy())
                return 

            curList.append(candidates[i])
            backtrack(i, curList, curSum + candidates[i])
            
            curList.pop()
            backtrack(i+1, curList, curSum)

        backtrack(0,[],0)
        
        return res
        
# @lc code=end


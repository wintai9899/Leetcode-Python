#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # cache: (index, curSum) : no. of ways to reach curSum
        dp = {}
        
        def backtrack(i, curSum):
            # base case: evaluated all elements
            if i == len(nums):
                # if found ways to reach target:
                if curSum == target:
                    return 1
                else:
                    return 0
            
            # if in cache
            if (i, curSum) in dp:
                return dp[(i,curSum)]

            dp[(i, curSum)] = backtrack(i+1,curSum + nums[i]) + backtrack(i+1, curSum - nums[i])
            return dp[(i,curSum)]
                
            
        return backtrack(0,0)
        
# @lc code=end


#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {} 
        
        def dfs(l,r):
            # no more balloons left
            if l > r:
                return 0
            
            if (l,r) not in dp:
                dp[(l,r)] = max([dfs(l, i-1) + nums[l-1] * nums[i] * nums[r+1] + dfs(i+1,r) for i in range(l,r+1)])
            return dp[(l,r)]
        # ignore arbituray 1s on both sides
        return dfs(1, len(nums) - 2)

        
        
# @lc code=end


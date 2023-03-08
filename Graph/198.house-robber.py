#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0
        
        for num in nums:
            maxRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = maxRob
        return rob2
        
# @lc code=end


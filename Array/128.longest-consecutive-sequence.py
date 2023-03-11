#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        
        for num in nums:
            length = 0
            if(num-1) not in numSet:
                while num + length in numSet:
                    length += 1
                
                res = max(res, length)
        
        return res
        
# @lc code=end


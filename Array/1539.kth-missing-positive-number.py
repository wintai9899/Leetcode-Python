#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arrSet = set(arr)
        
        for i in range(len(arr) + 1 + k):
            if i not in arrSet:
                k -= 1
            
            if k == 0:
                return i
        
# @lc code=end


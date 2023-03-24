#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (66.11%)
# Likes:    13460
# Dislikes: 665
# Total Accepted:    1.7M
# Total Submissions: 2.6M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
# 
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
# 
# You must solve it in O(n) time complexity.
# 
# 
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        res = 0
        for num in nums:
            num *= -1
            heapq.heappush(maxHeap,num)
        
        for _ in range(k):
            res = heapq.heappop(maxHeap)
        
        return -res
        
# @lc code=end


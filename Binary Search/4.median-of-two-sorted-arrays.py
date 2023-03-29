#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (36.06%)
# Likes:    22747
# Dislikes: 2556
# Total Accepted:    1.8M
# Total Submissions: 5.1M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
# 
# The overall run time complexity should be O(log (m+n)).
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# 
# 
# 
# Constraints:
# 
# 
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #  nums1 = [1,2,3,4,5,6,7,8]   nums2 = [1,2,3,4,5]
        # A = nums2 = [1,2,3,4,5], B = nums1 = [1,2,3,4,5,6,7,8]
        # total = 13, half = 13 // 2 = 6
        # Binary search using A (the shorted array)
        #      L   M   R
        # A = [1,2,3,4,5] -> [1,   2,   3,      4,   5]
        #                    < --------->       <----->
        #                             Aleft   Aright
        # B = [1,2,3,4,5,6,7,8] 
        # [1,   2,   3,         4,   5,   6,   7,  8]
        # <----------->        <-------------------->
        #         BLeft         Bright
        # If partitioned correctly:
        # 1. Aleft <= Bright and Bleft <= ARight
        # If odd lengths: median = min(Aright, Bright)
        # If even lengths: median = (max(Bleft, Aleft) + min(Aright,Bright)) / 2

        A = nums1
        B = nums2 

        if len(B) < len(A):
            A, B = B, A
        
        totalLength = len(nums1) + len(nums2)
        half = totalLength // 2

        # pointers for A
        l,r = 0, len(A)-1

        while True:
            # partition point for A
            i = (l + r) // 2
            # partition point for b
            j = half - i - 2

            # rightMost value in the leftSubaaray of A
            ALeft = A[i] if i >= 0 else float("-inf")
            # leftMost value in the rightSubarray of A
            ARight = A[i+1] if (i+1) < len(A) else float("inf")
            
            # rightMost value in the leftSubaaray of B
            BLeft = B[j] if j >= 0 else float("-inf")
            # leftMost value in the rightSubarray of B
            BRight = B[j+1] if (j+1) < len(B) else float("inf")

            # partionioned correctly
            if ALeft <= BRight and BLeft <= ARight:
                # if odd length
                if totalLength % 2 != 0:
                    median = min(ARight, BRight)
                    return median
                # evem
                else:
                    median = (max(ALeft, BLeft) + min(ARight,BRight)) /2
                    return median


            # partionioned wrong: ALeft is too big
            elif ALeft > BRight:
                r -= 1
            
            else: 
                l += 1
        
# @lc code=end


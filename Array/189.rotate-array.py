#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = k % len(num) = 3 % 7 = 3
        # 1. partition into two parts -> nums[0:k] and nums[k:-1]
        #  l        k        r
        # [1, 2, 3, 4, 5, 6, 7] 
        # <-  A ->  <-   B   ->
        # 2. Reverse entire array
        # l         k        r
        # [7, 6, 5, 4, 3, 2, 1] 
        # <-  A  -> <-   B   ->
        # 3. reverse subarray A 
        #  l        k        r
        # [5, 6, 7, 4, 3, 2, 1] 
        # <-  A  -> <-   B   ->
        # 4. reverse subarray B 
        # l        k        r
        # [5, 6, 7, 1, 2, 3, 4] 
        # <-  A  ->  <-   B   ->
        n = len(nums) 
        k = k % n 

        self.reverse(0,n-1,nums)
        self.reverse(0,k-1,nums)
        self.reverse(k,n-1, nums)


    def reverse(self, start, end, nums):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
# @lc code=end


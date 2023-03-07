#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        nums.sort()
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index-1]:
                continue 
            
            l = index +  1
            r = len(nums) - 1 
            
            while l < r:
                totalSum = value + nums[l] + nums[r]
                if totalSum < 0:
                    l += 1
                
                elif totalSum > 0:
                    r -= 1 
                
                else:
                    candidate = [nums[r], nums[l], value]
                    res.append(candidate)
                    
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    
                    l += 1
        return res
        
# @lc code=end


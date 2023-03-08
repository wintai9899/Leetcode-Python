#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        maxProfit = 0
        
        for r in range(len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                if profit > maxProfit:
                    maxProfit = profit
            
            else:
                l = r
        
        return maxProfit        
# @lc code=end


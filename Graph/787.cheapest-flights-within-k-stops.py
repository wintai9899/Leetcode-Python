#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # create price table for src node 
        prices = [float("inf")] * n
        # start froms src node
        prices[src] = 0
        
        for i in range(k + 1):
            tempPrice = prices.copy()
            
            for s, d, p, in flights:
                # if not reacheable
                if prices[s] == float("inf"):
                    continue
                
                # if found cheaper prices
                if prices[s] + p < tempPrice[d]:
                    tempPrice[d] =  prices[s] + p
                
            # update price table
            prices = tempPrice

        return prices[dst] if prices[dst] != float("inf") else -1
                
        
        
        
# @lc code=end


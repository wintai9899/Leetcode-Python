#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} 
        res = []
        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
            
        maxHeap = [(-freq, num) for num,freq in hashmap.items()]
        heapq.heapify(maxHeap)
        
        for _ in range(k):
            # returns a tuple : (-freq, num)
            num = heapq.heappop(maxHeap)[1]
            res.append(num)
        
        return res
                    
        
# @lc code=end


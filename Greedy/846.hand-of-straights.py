#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#
# https://leetcode.com/problems/hand-of-straights/description/
#
# algorithms
# Medium (56.23%)
# Likes:    1919
# Dislikes: 142
# Total Accepted:    114.5K
# Total Submissions: 203.8K
# Testcase Example:  '[1,2,3,6,2,3,4,7,8]\n3'
#
# Alice has some number of cards and she wants to rearrange the cards into
# groups so that each group is of size groupSize, and consists of groupSize
# consecutive cards.
# 
# Given an integer array hand where hand[i] is the value written on the i^th
# card and an integer groupSize, return true if she can rearrange the cards, or
# false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
# 
# 
# Example 2:
# 
# 
# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= hand.length <= 10^4
# 0 <= hand[i] <= 10^9
# 1 <= groupSize <= hand.length
# 
# 
# 
# Note: This question is the same as 1296:
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
# 
#

# @lc code=start
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # group divisible by groupSize 
        if len(hand) % groupSize != 0:
            return False 

        # count occurrence of all cards
        # {1: 1, 2: 2, 3: 2, 6: 1, 4: 1, 7: 1, 8: 1}
        hashmap = {}
        for h in hand:
            hashmap[h] = hashmap.get(h,0) + 1
        
        # use MinHeap to find the current minimum card, NOT sort by occurence
        minHeap = list(hashmap.keys())
        heapq.heapify(minHeap)

        while minHeap:
            # start of the consecituve elements in subgroup
            firstElement = minHeap[0]
            # search for consecutive elements: 
            for i in range(firstElement, firstElement + groupSize):
                if firstElement not in hashmap:
                    return False 
                
                hashmap[firstElement] -= 1
                
                # remove from heap if all used
                if hashmap[firstElement] == 0:
                    # not possible for build next subgroup
                    if firstElement != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        
        return True
        
# @lc code=end


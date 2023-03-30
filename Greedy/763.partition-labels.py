#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
# https://leetcode.com/problems/partition-labels/description/
#
# algorithms
# Medium (79.76%)
# Likes:    9321
# Dislikes: 345
# Total Accepted:    459.4K
# Total Submissions: 576.3K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# You are given a string s. We want to partition the string into as many parts
# as possible so that each letter appears in at most one part.
# 
# Note that the partition is done so that after concatenating all the parts in
# order, the resultant string should be s.
# 
# Return a list of integers representing the size of these parts.
# 
# 
# Example 1:
# 
# 
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits s into less parts.
# 
# 
# Example 2:
# 
# 
# Input: s = "eccbbbbdec"
# Output: [10]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 500
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # get lastIndex of every char in s
        lastIndex = {}

        for i,c in enumerate(s):
            lastIndex[c] = i 
        
        # size of partition
        size = 0
        # end of current partition
        curEnd = 0
       
        res = []
        for i,c in enumerate(s):
            size += 1
            # found char position outside of cur partion
            if lastIndex[c] > curEnd:
                curEnd = lastIndex[c]
            # partitioned successfully
            if i == curEnd:
                res.append(size)
                # reset size 
                size = 0

       
        return res
                
        
# @lc code=end


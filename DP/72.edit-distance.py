#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (54.34%)
# Likes:    12210
# Dislikes: 142
# Total Accepted:    633.3K
# Total Submissions: 1.2M
# Testcase Example:  '"horse"\n"ros"'
#
# Given two strings word1 and word2, return the minimum number of operations
# required to convert word1 to word2.
# 
# You have the following three operations permitted on a word:
# 
# 
# Insert a character
# Delete a character
# Replace a character
# 
# 
# 
# Example 1:
# 
# 
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# 
# 
# Example 2:
# 
# 
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# 
# 
# 
# Constraints:
# 
# 
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # case1: word1 = "", word2 = "abc" -> operations = len(word2) 
        # case2: word1 = "abc", word2 = "" -> operations = len(word1) 

        # case3: if word1[i] == word2[j] -> (i+1,j+1)
        # case 4: else: 
        # insert: move pointer of word2 -> (i,j+1)
        # delete: move pointer of word 1 -> (i+1,j)
        # replace: move both pointers -> (i+1, j+1)

        # dp[r][c] = num. of operations for this subproblem
        cache = [[float("inf") for i in range(len(word2)+1)] for j in range(len(word1)+1)]

        # case2
        for j in range(len(word2)+1):
            cache[len(word1)][j] = len(word2) - j
        
        # case 1
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                
                else:
                    # insert or delete or replace
                    insert = cache[i][j + 1]
                    delete = cache[i+1][j]
                    replace = cache[i+1][j+1]
                    cache[i][j] = 1 + min(insert, delete, replace)
        return cache[0][0]
        
# @lc code=end


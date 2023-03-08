#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        # at least 1 decode way
        dp[len(s)] = 1
        
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                dp[i] = 0
            
            else:
                dp[i] = dp[i+1]
            
            # handle double digit
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                dp[i] += dp[i+2]
        
        return dp[0]
        
        
# @lc code=end


"""
s = ""226""  -> "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
output = 3

at least one decode way so dp[len(s)] = 1
dp = [0, 0, 0, 1]

iterate reverse
        i
s = 2 2 6

dp[i] = dp[i+1]
-> dp = [0, 0, 1, 1]

      i
s = 2 2 6

dp[i] = dp[i+1]
then if double digits: dp[i] += dp[i+2]

-> dp = [0, 2, 1, 1]

    i
s = 2 2 6

dp[i] = dp[i+1]

-> dp = [2, 2, 1, 1]

if double digits: dp[i] += dp[i+2]
-> dp = [3, 2, 1, 1]

output = dp[0] = 3


"""
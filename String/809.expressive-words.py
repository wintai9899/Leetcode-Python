#
# @lc app=leetcode id=809 lang=python3
#
# [809] Expressive Words
#

# @lc code=start
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        res = 0
        
        def isStretchy(word):
            
            # pointer for word
            j = 0
            
            for i in range(len(s)):
                # handles first e
                if j < len(word) and s[i] == word[j]:
                    j += 1
                #                    i
                # skip duplicates: e e e
                elif 0 < i < len(s) - 1 and s[i-1] == s[i] == s[i+1]:
                    continue
                #                      i
                # skip duplicates: e e e
                elif i > 1 and s[i] == s[i-1] == s[i-2]:
                    continue 
                # not stretchable
                else:
                    return 0
            
            return 1 if j == len(word) else 0
                
                
        
        for word in words:
            res += isStretchy(word)
        
        return res
    
   
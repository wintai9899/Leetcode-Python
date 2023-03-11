#
# @lc app=leetcode id=691 lang=python3
#
# [691] Stickers to Spell Word
#

# @lc code=start
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # stickCount = [{'w': 1, 'i': 1, 't': 1, 'h': 1}, 
        # {'e': 2, 'x': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1}, 
        # {'s': 1, 'c': 2, 'i': 1, 'e': 2, 'n': 1}]
        stickCount = [] 

        for i,s in enumerate(stickers):
            wordCount= {}
            for c in s:
                wordCount[c] = wordCount.get(c,0) + 1
            stickCount.append(wordCount)
        # cache
        dp = {} 

        # greedy approach: try to exhaust every character in the sticker before moving on. 
        
        def dfs(targetStr, sticker):
            if targetStr in dp:
                return dp[targetStr]
            res = 1 if sticker else 0
            remainTarget = ""
            for c in targetStr:
                # if character in sticker, cut it off
                if c in sticker and sticker[c] >0:
                    sticker[c] -= 1
                
                else:
                    # if character not in sticker, add to remainderString for evaluation later
                    remainTarget += c
            # continue searching recursiverly is remainderStr is not empty. 
            if remainTarget:
                used = float("inf")
                # go through every hashmap in stickerCount
                for s in stickCount:
                    if remainTarget[0] not in s:
                        continue
                    used = min(used, dfs(remainTarget, s.copy()))
                # store in cache
                dp[remainTarget] = used
                # added used stickers to result. 
                res += used
            return res
        
        res = dfs(target, {})
        return res if res != float("inf") else -1
            
        
# @lc code=end


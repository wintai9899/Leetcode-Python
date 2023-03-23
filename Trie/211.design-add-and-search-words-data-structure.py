#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
#
# algorithms
# Medium (43.00%)
# Likes:    6749
# Dislikes: 383
# Total Accepted:    517.4K
# Total Submissions: 1.2M
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
  '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports adding new words and finding if a
# string matches any previously added string.
# 
# Implement the WordDictionary class:
# 
# 
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched
# later.
# bool search(word) Returns true if there is any string in the data structure
# that matches word or false otherwise. word may contain dots '.' where dots
# can be matched with any letter.
# 
# 
# 
# Example:
# 
# 
# Input
# 
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
# 
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
# 
# 
# 
# Constraints:
# 
# 
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 3 dots in word for search queries.
# At most 10^4 calls will be made to addWord and search.
# 
# 
#

# @lc code=start
class TrieNode():
  
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curNode = self.root
        
        for c in word:
            if c not in curNode.children:
                curNode.children[c] = TrieNode()
              
            curNode = curNode.children[c]
        
        curNode.endOfWord = True
        
    def search(self, word: str) -> bool:
        def dfs(idx, node):
            curNode = node 
            
            for i in range(idx, len(word)):
                c = word[i]
                # backtrack
                if c == ".":
                    for child in curNode.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                # iterative search
                else:
                    if c not in curNode.children:
                        return False
                      
                    curNode = curNode.children[c]

            return curNode.endOfWord
          
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end


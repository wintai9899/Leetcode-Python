#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [0] * (n+1)
        
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                res[i] = "FizzBuzz"
            
            elif i % 3 == 0:
                res[i] = "Fizz"
            
            elif i % 5 == 0:
                res[i] = 'Buzz'
            
            else:
                res[i] = str(i)
                
        res.pop(0)
        
        return res        
# @lc code=end


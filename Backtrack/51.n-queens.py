#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        colSet = set()
        posDiag = set()
        negDiag = set()
        board = [["." for _ in range(n)] for _ in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = []
                for row in board:
                    rowData = "".join(row)
                    copy.append(rowData)
                res.append(copy)
                
            for c in range(n):
                if c in colSet or (r+c) in posDiag or (r-c) in negDiag:
                    continue
            
                colSet.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                
                backtrack(r+1)
                
                #clean up 
                colSet.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res
                    
                
# @lc code=end


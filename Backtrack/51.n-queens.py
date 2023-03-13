#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Q moves in horizontal, vertical, and diagonal in both directions 
        # only 1 queen in each row 
        # only 1 queen in each col 
        # only 1 queen in each positive diagonal 
        # only 1 queen in each negative diagonal 

        # to check if a queen exists negative diagonals (downwards): 
        # eg. start from (0,0) -> (1,1) -> (2,2) -> (3,3)   r-c = 0
        # eg. start from (0,1) -> (1,2) -> (2,3) ->         r-c = 1
        # (r-c) is constant for every decreasing diagonal move
        # if (current r - current c) in negDiagSet: continue

        # to check if a queen exists in positive diagonals (upwards): 
        # eg. start from (3,0) -> (2,1) -> (1,2) -> (0,3)   r+c = 3
        # eg. start from (3,1) -> (2,2) -> (1,3) ->         r+c = 4
        # (r+c) is constant for every increasing diagonal move
        # if (current r + current c) in posDiagSet: continue

        
        res = []
        colSet = set()
        posDiag = set()
        negDiag = set()
        board = [["." for _ in range(n)] for _ in range(n)]
        # backtrack for every row
        def backtrack(r):
            # able to place all queens 
            if r == n:
                copy = []
                for row in board:
                    # ['.', '.', 'Q', '.'] -> "..Q."
                    rowData = "".join(row)
                    copy.append(rowData)
                res.append(copy)
            # iterate the cols
            # no need to iterate rows as we are backtracking based on rows
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


#
# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#

# @lc code=start
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # iterate through every elements
        # only count the "head" of the ship, we can skip the "body" as we know its the same ship
        ROWS = len(board)
        COLS = len(board[0])
        res = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "X":
                    # if board[r][c] is body of a ship, continue 
                    if r > 0 and board[r-1][c] == "X":
                        continue
                    
                    if c > 0 and board[r][c-1] == "X":
                        continue
                    
                    # if its the head of the ship, increment count and continue
                    # vertical ships
                    # either the head is at the first row, or there is a "." above it, meaning its a head of a battleship
                    if r == 0 or board[r-1][c] == ".":
                        res += 1
                    
                    # horizontal ships
                    # either the head is at the col row, or there is a "." on the left it, meaning its a head of a battleshi
                    elif c == 0 or board[r][c-1] == '.':
                        res += 1
        return res        
# @lc code=end


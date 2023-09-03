from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check horizontal
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] != '.':
                    if board[r][c] in seen: return False
                    seen.add(board[r][c])

        # check vertical
        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] != '.':
                    if board[r][c] in seen: return False
                    seen.add(board[r][c])

        # check square
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                seen = set()
                for i in range(9):
                    cur = board[r+i//3][c+i%3]
                    if cur == '.': continue
                    if cur in seen: return False
                    seen.add(cur)
    
        return True
    
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_seen = defaultdict(set) # vertical
        c_seen = defaultdict(set) # horizontal
        s_seen = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if board[r][c] in c_seen[c]:
                    return False
                if board[r][c] in r_seen[r]:
                    return False
                if board[r][c] in s_seen[(r//3, c//3)]:
                    return False
                
                r_seen[r].add(board[r][c])
                c_seen[c].add(board[r][c])
                s_seen[(r//3,c//3)].add(board[r][c])
        
        return True
        
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        temp = [[c for c in row] for row in board]
        m, n = len(board), len(board[0])

        for r in range(m):
            for c in range(n):
                one = 0
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if not dr and not dc: continue
                        if r+dr < 0 or r+dr >= m or c+dc < 0 or c+dc >= n: continue
                        if temp[r+dr][c+dc] == 1: one += 1

                if temp[r][c] == 1:
                    if one not in (2, 3):
                        board[r][c] = 0
                else:
                    if one == 3:
                        board[r][c] = 1

# O(1) space.
# 11 > live current, live next
# 10 > dead current, live next

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        for r in range(m):
            for c in range(n):
                one = 0
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if not dr and not dc: continue
                        if r+dr < 0 or r+dr >= m or c+dc < 0 or c+dc >= n: continue
                        one += board[r+dr][c+dc] & 1

                if board[r][c] & 1 == 1:
                    if one == 2 or one == 3:
                        board[r][c] = 0b11
                else:
                    if one == 3:
                        board[r][c] = 0b10
        
        for r in range(m):
            for c in range(n):
                board[r][c] >>= 1
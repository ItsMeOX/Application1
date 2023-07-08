from typing import List
from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        lo, hi = 0, len(cells)

        def canCross(i):
            grid = [[0]*col for _ in range(row)]
            directions = [(1, 0),(-1, 0),(0, -1),(0, 1)]
            for j in range(i):
                r, c = cells[j]
                grid[r-1][c-1] = 1
            q = deque()
            for j in range(col):
                if grid[0][j] == 0:
                    grid[0][j] = -1
                    q.append((0,j))

            while q:
                r, c = q.popleft()
                if r == row-1:
                    return True
                for dr, dc in directions:
                    if 0 <= r+dr < row and 0 <= c+dc < col and grid[r+dr][c+dc] != -1 and grid[r+dr][c+dc] != 1:
                        q.append((r+dr, c+dc))

            return False



        while lo <= hi:
            m = (lo+hi) // 2
            if canCross(m): # if still can cross, answer is between idx m to last
                lo = m + 1
            else:
                hi = m - 1 # else, answer is between idx 0 to m - 1

        return lo - 1
    
        # or 
        
        # while lo < hi:
        #     m = hi - (hi - lo) // 2
        #     if canCross(m): # if still can cross, answer is between idx m to last
        #         lo = m
        #     else:
        #         hi = m - 1 # else, answer is between idx 0 to m - 1

        # return lo
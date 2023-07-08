from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque() # (row, col, distance)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n = len(grid)
        res = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
        
        if not q:
            return -1

        while q:
            for _ in range(len(q)):
                row, col, distance = q.popleft()
                res = max(res, distance)
                for drow, dcol in directions:
                    if 0 <= drow+row < n and 0 <= dcol+col < n and grid[drow+row][dcol+col] == 0:
                        q.append((drow+row, dcol+col, distance + abs(drow) + abs(dcol)))
                        grid[drow+row][dcol+col] = -1
    
        return -1 if not res else res
        

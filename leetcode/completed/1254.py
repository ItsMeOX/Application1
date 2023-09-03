from typing import List

# For every unvisited island, if there is a cell which is at the border of the matrix, then it is not closed,
# otherwise it is closed.

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        directions = ((-1, 0),(1, 0),(0, -1),(0, 1))
        q = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    closed = True
                    q.append((i, j))
                    grid[i][j] = -1
                    while q:
                        r, c = q.pop()
                        for dr, dc in directions:
                            if r+dr < 0 or r+dr >= m or c+dc < 0 or c+dc >= n:
                                closed = False
                                continue
                            if grid[r+dr][c+dc] == 0:
                                grid[r+dr][c+dc] = -1
                                q.append((r+dr, c+dc))
                    if closed:
                        res += 1
        return res
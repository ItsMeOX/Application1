from typing import List

# Count every '1' from grid and store the number of '1' in variable count_one.
# Start an BFS from boundary cell, we subtract count_one every time we meet a '1'.
# The remaning count_one will be number of cell which we can't walk off the boundary.

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        one_count = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        for row in grid:
            one_count += row.count(1)
        
        q = []

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and grid[i][j]:
                    q.append((i, j))
                    grid[i][j] = 0
                    while q:
                        row, col = q.pop()
                        one_count -= 1
                        for drow, dcol in directions:
                            if 0 <= drow+row < m and 0 <= dcol+col < n and grid[drow+row][dcol+col]:
                                grid[drow+row][dcol+col] = 0     # We have to mark cell as visited here if we are not using popleft.
                                q.append((drow+row, dcol+col))
        
        return one_count
from typing import List

# Just perform BFS / DFS and only traverse val of grid of next move == current val + 1.
# If no grid are valid, then return false.
# If 'cur' reaches n*n-1, then return True.

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0]: return False

        directions = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
        n = len(grid)

        def dfs(r, c, cur):
            if cur == n * n - 1:
                return True

            for dr, dc in directions:
                if 0 <= r+dr < n and 0 <= c + dc < n and grid[r+dr][c+dc] == cur+1:
                    return dfs(r+dr, c+dc, cur+1)
            
            return False
        
        return dfs(0, 0, 0)
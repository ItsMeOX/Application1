from typing import List
from heapq import heappop, heappush

# Cannot only use BFS here. (?)
# Using Dijsktra's algorithm here,
# Starting from start, traverse to left, top, right, bottom.
# If the next pos is box, then update box pos.
# If box_row == target_row and box_col == target_col, return res.
# Note that we do not need to consider 'res' for visited set, as 
# box_row and box_col will be different after moving the box.

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        directions = ((-1, 0),(1, 0),(0, -1),(0, 1))

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 'S':
                    player_r, player_c = r, c
                elif grid[r][c] == 'T':
                    target_r, target_c = r, c
                elif grid[r][c] == 'B':
                    box_r, box_c = r, c
        
        def isValid(r, c):
            return 0 <= r < m and 0 <= c < n and grid[r][c] != '#'

        q = [] # (player_r, player_c, box_r, box_c, pushes)
        q.append((0, player_r, player_c, box_r, box_c))
        
        while q:
            res, r, c, b_r, b_c = heappop(q)

            if b_r == target_r and b_c == target_c:
                return res

            for dr, dc in directions:
                if isValid(r+dr, c+dc):
                    if r+dr == b_r and c+dc == b_c:
                        if isValid(r+2*dr, c+2*dc) and (r+dr, c+dc, r+2*dr, c+2*dc) not in visited:
                            visited.add((r+dr, c+dc, r+2*dr, c+2*dc))
                            heappush(q, (res+1, r+dr, c+dc, r+2*dr, c+2*dc))
                    else:
                        if (r+dr, c+dc, b_r, b_c) not in visited:
                            visited.add((r+dr, c+dc, b_r, b_c))
                            heappush(q, (res, r+dr, c+dc, b_r, b_c))
        
        return -1
    
sol = Solution()
grid = [
    [".",".","#",".",".",".",".",".",".","."],
    [".","#",".","#","B","#",".","#",".","."],
    [".","#",".",".",".",".",".",".","T","."],
    ["#",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","#"],
    [".",".",".",".",".",".",".",".","#","."],
    [".",".",".","#",".",".","#","#",".","."],
    [".",".",".",".","#",".",".","#",".","."],
    [".","#",".","S",".",".",".",".",".","."],
    ["#",".",".","#",".",".",".",".",".","#"]
]
print(sol.minPushBox(grid))
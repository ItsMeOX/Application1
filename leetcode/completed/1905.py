from typing import List

# Explore every island in grid2, mark the island as visited.
# If the island land in grid1 == 0, then set flag = False.
# if flag == True, then add 1 to res.

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        directions = ((-1, 0),(1, 0),(0, -1),(0, 1))
        q = []
        res = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    flag = True
                    q.append((i, j))
                    grid2[i][j] = -1
                    while q:
                        r, c = q.pop()
                        if grid1[r][c] != 1:
                            flag = False
                        for dr, dc in directions:
                            if 0 <= r+dr < m and 0 <= c+dc < n and grid2[r+dr][c+dc] == 1:
                                grid2[r+dr][c+dc] = -1
                                q.append((r+dr, c+dc))
                    if flag: res += 1
    
        return res
from typing import List
from collections import deque

# Start BFS from every top left corner, 
# the first explore cell will be the top left rect,
# the last explored cell will be the bottom right rect.

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        m, n = len(land), len(land[0])
        directions = ((1, 0),(0, 1))
        q = deque()

        for r in range(m):
            for c in range(n):
                if land[r][c] == 1:
                    q.append((r, c))
                    rect = [r, c, 0, 0]
                    land[r][c] = -1
                    while q:
                        r2, c2 = q.popleft()
                        rect[-2] = r2
                        rect[-1] = c2
                        for dr, dc in directions:
                            if r2+dr < m and c2+dc < n and land[r2+dr][c2+dc] == 1:
                                land[r2+dr][c2+dc] = -1
                                q.append((r2+dr, c2+dc))
                    res.append(rect)

        return res
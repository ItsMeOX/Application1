from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        pacific = set()
        atlantic = set()
        res = []

        q = []
        q.append((0, 0))
        pacific.add((0, 0))
        while q:
            r, c = q.pop()
            for dr, dc in directions:
                if 0 <= r+dr < m and 0 <= c+dc < n:
                    if (heights[r+dr][c+dc] >= heights[r][c] or r+dr == 0 or c+dc == 0) and (r+dr, c+dc) not in pacific:
                        pacific.add((r+dr, c+dc))
                        q.append((r+dr, c+dc))                

        q.append((m-1, n-1))
        atlantic.add((m-1, n-1))
        while q:
            r, c = q.pop()
            for dr, dc in directions:
                if 0 <= r+dr < m and 0 <= c+dc < n:
                    if (heights[r+dr][c+dc] >= heights[r][c] or r+dr == m-1 or c+dc == n-1) and (r+dr, c+dc) not in atlantic:
                        atlantic.add((r+dr, c+dc))
                        q.append((r+dr, c+dc))                

        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res
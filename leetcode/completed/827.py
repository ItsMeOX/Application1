from typing import List

# Union two cells if they are both 1 and are adjacent.
# Also, find all the edges of islands.
# From all the edges, perform BFS and check if neighbour cells are 0,
# if it is then from the 0 valued cell, check if neighbour cells are 1.
# If true then check if this island is not the island we discovered from, 
# and add the size of the neighbour island to size of current island.
# Update res the maximum current island size.

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # [0,1,2], [3,4,5]
        # [0,1,2,3,4,5]

        par = [i for i in range(m*n)]
        rank = [1] * (m*n)
        directions = ((-1, 0),(1, 0),(0, -1),(0, 1))

        def find(a):
            t = a
            while t != par[t]:
                t = par[t]
            par[a] = t
            return t
        
        def union(a, b):
            ar, br = find(a), find(b)
            if ar == br: return
            if rank[ar] > rank[br]:
                par[br] = ar
                rank[ar] += rank[br]
            else:
                par[ar] = br
                rank[br] += rank[ar]
        
        q = []

        # union & find edge
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0: continue
                added = False
                for dr, dc in directions:
                    if 0 <= r+dr < m and 0 <= c+dc < n:
                        if grid[r+dr][c+dc] == 1:
                            union((r+dr)*m+c+dc, r*m+c)
                        else:
                            if not added:
                                added = True
                                q.append((r, c))
        
        if not q: 
            if grid[0][0] == 1:
                return m*n
            return 1
        res = 0

        while q:
            r, c = q.pop()
            for dr, dc in directions:
                if 0 <= r+dr < m and 0 <= c+dc < n and grid[r+dr][c+dc] == 0:
                    nr, nc = r+dr, c+dc
                    total = rank[find(r*m+c)]
                    found_root = [find(r*m+c)]
                    for dr, dc in directions:
                        if 0 <= dr+nr < m and 0 <= dc+nc < n and grid[dr+nr][dc+nc] == 1:
                            root = find((nr+dr)*m+nc+dc)
                            if root in found_root: continue
                            found_root.append(root)
                            total += rank[root]
                    res = max(res, total + 1)

        return res
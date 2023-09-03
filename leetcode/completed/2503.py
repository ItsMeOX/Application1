from typing import List
from collections import deque, defaultdict
from heapq import heappop, heappush

# Sort queries first from smallest to largest.
# Utilize min heap here, 
# starting from (0, 0), we always explore the current smallest-valued grid first,
# if the current smallest-valued >= min val in heap, then the answer for the min val
# will be the current covered grids.

# Note that after exploring all the grids, we might have left over query that is >= all val in grid.

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = [0] * len(queries)
        directions = ((-1, 0),(1, 0),(0, -1),(0, 1))

        indices = defaultdict(list) # Could actually be optimized for this part
        for i in range(len(queries)):
            indices[queries[i]].append(i)
        queries = deque(sorted(set(queries)))

        heap = [(grid[0][0], 0, 0)] # val, r, c
        grid[0][0] = -1
        covered = 0

        while heap:
            val, r, c = heappop(heap)
            while queries and val >= queries[0]:
                for idx in indices[queries.popleft()]:
                    res[idx] = covered        
            covered += 1
            for dr, dc in directions:
                if 0 <= r+dr < m and 0 <= c+dc < n and grid[r+dr][c+dc] != -1:
                    heappush(heap, (grid[r+dr][c+dc], r+dr, c+dc))
                    grid[r+dr][c+dc] = -1
        
        while queries: # queries that are >= all the values in grid
            for idx in indices[queries.popleft()]:
                res[idx] = covered        

        return res
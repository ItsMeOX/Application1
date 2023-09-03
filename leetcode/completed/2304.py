from typing import List
from heapq import heappop, heappush

# For every node at row = 0, perform a Dijsktra's algorithm and find the shortest path
# to any bottom nodes.

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        distance = [[float('inf')]*n for _ in range(m)] 

        heap = []
        for c in range(n):
            heappush(heap, (grid[0][c], 0, c))
            distance[0][c] = grid[0][c]

        while heap:
            cur_cost, r, c = heappop(heap)
            if cur_cost != distance[r][c]:
                continue
            
            if r == m-1:
                return cur_cost

            for i in range(n):
                new_cost = cur_cost + moveCost[grid[r][c]][i] + grid[r+1][i]
                if new_cost < distance[r+1][i]:
                    distance[r+1][i] = new_cost
                    heappush(heap, (new_cost, r+1, i))

from functools import lru_cache
# DFS - top down approach
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(r, c):
            if r == m-1:
                return grid[r][c]
            
            t = float('inf')
            for i in range(n):
                t = min(t, dfs(r+1, i) + moveCost[grid[r][c]][i])

            return t + grid[r][c]
        
        res = float('inf')
        for c in range(n):
            res = min(res, dfs(0, c))
        
        return res

# Here it is wrong because we have added a grid twice (+grid[r+1][i] and +grid[r][c])  
# def dfs(r, c):
#     if r == m-1:
#         return 0
    
#     t = float('inf')
#     for i in range(n):
#         t = min(t, dfs(r+1, i) + grid[r+1][i] + moveCost[grid[r][c]][i])
    
#     return t + grid[r][c]

# DP - bottom up approach
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dpb = [0] * n

        for c in range(n):
            dpb[c] = grid[-1][c]

        for r in range(m-2, -1, -1):  
            dpf = [float('inf')] * n
            for c in range(n):
                for i in range(n):
                    dpf[c] = min(dpf[c], dpb[i] + moveCost[grid[r][c]][i])
                dpf[c] += grid[r][c]
            dpb = dpf

        return min(dpf)
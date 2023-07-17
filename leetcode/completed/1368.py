from typing import List
from heapq import heappop, heappush

class Solution:
    def minCost(self, grid: List[List[int]]) -> int: # heap
        m, n = len(grid), len(grid[0])

        q = [] # (cost, row, col)
        q.append((0, 0, 0))

        visited = {}

        free = {
            ( 0,  1): 1,
            ( 0, -1): 2,
            ( 1,  0): 3,
            (-1,  0): 4
        }

        directions = ((0, 1),(0, -1),(1, 0),(-1, 0))

        while q:
            cost, r, c = heappop(q)
            if r == m-1 and c == n-1:
                return cost

            for dr, dc in directions:
                if 0 <= r+dr < m and 0 <= c+dc < n and (r+dr, c+dc):
                    if (r+dr, c+dc) in visited and visited[(r+dr, c+dc)] <= cost:
                        continue
                    if free[(dr, dc)] == grid[r][c]:
                        heappush(q, (cost, r+dr, c+dc))
                        visited[(r+dr, c+dc)] = cost
                    else:
                        heappush(q, (cost+1, r+dr, c+dc))
                        visited[(r+dr, c+dc)] = cost + 1

from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int: # 0, 1 BFS
        m, n = len(grid), len(grid[0])

        q = deque()
        q.append((0, 0, 0))

        visited = {}

        free = {
            ( 0,  1): 1,
            ( 0, -1): 2,
            ( 1,  0): 3,
            (-1,  0): 4
        }

        directions = ((0, 1),(0, -1),(1, 0),(-1, 0))

        while q:
            cost, r, c = q.popleft()
            if r == m-1 and c == n-1:
                return cost

            for dr, dc in directions:
                if 0 <= r+dr < m and 0 <= c+dc < n and (r+dr, c+dc):
                    if (r+dr, c+dc) in visited and visited[(r+dr, c+dc)] <= cost:
                        continue
                    if free[(dr, dc)] == grid[r][c]:
                        q.appendleft((cost, r+dr, c+dc))
                        visited[(r+dr, c+dc)] = cost
                    else:
                        q.append((cost+1, r+dr, c+dc))
                        visited[(r+dr, c+dc)] = cost + 1
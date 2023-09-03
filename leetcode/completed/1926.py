from collections import deque
from typing import List

# Just perform BFS and find the shortest path.
# Here we can either initialize a visited set or just mark the visited grid to '+' after we visit a grid.

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        start_r, start_c = entrance
        m, n = len(maze), len(maze[0])

        q = deque()
        q.append((start_r, start_c))

        res = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r != start_r or c != start_c) and (r in (0, m-1) or c in (0, n-1)):
                    return res
                
                for dr, dc in directions:
                    if 0 <= r+dr < m and 0 <= c+dc < n and maze[r+dr][c+dc] == '.':
                        maze[r+dr][c+dc] = '+'
                        q.append((r+dr, c+dc))
            res += 1
            
        return -1
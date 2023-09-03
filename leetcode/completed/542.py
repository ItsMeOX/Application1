from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        directions = ((-1, 0),(1, 0),(0, -1),(0, 1))
        # find border
        q = deque()
        visited = set()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0: continue
                for dr, dc in directions:
                    if 0 <= r + dr < m and 0 <= c + dc < n and mat[r+dr][c+dc] == 0:
                        q.append((r, c))
                        visited.add((r, c))
                        break

        level = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                mat[r][c] = level
                for dr, dc in directions:
                    if 0 <= r+dr < m and 0 <= c + dc < n and mat[r+dr][c+dc] == 1:
                        if (r+dr, c+dc) not in visited:
                            visited.add((r+dr, c+dc))
                            q.append((r+dr, c+dc))
            level += 1
        
        return mat
    
# Optimization: start BFS from zeros, mark 1 as -1 (unvisited).

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        directions = ((-1, 0),(1, 0),(0, -1),(0, 1))

        q = deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1

        level = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if 0 <= r+dr < m and 0 <= c + dc < n and mat[r+dr][c+dc] == -1:
                        mat[r+dr][c+dc] = level
                        q.append((r+dr, c+dc))
            level += 1
        
        return mat
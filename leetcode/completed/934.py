from typing import List
from collections import deque

# Perform BFS / DFS on grid the first time and find the first island and append all the edges of first island to first q.
# Perform another BFS and find the shortest path from island 1 to island 2.

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        q1 = deque()
        q2 = deque()

        # find edges of first island
        for i in range(n):
            if 1 in grid[i]:
                q1.append((i, grid[i].index(1)))
                grid[i][grid[i].index(1)] = 2
                while q1:
                    row, col = q1.popleft()
                    isEdge = False
                    for drow, dcol in directions:
                        if 0 <= drow + row < n and 0 <= dcol + col < n: 
                            if grid[row+drow][col+dcol] == 1:
                                q1.append((drow+row, dcol+col))
                                grid[drow+row][dcol+col] = 2
                            elif grid[row+drow][col+dcol] == 0: # If there is atleast one water neighbour grid, it means this grid is edge of first island.
                                isEdge = True
                    if isEdge:
                        q2.append((row, col))
                break

        # find shortest bridge
        # can perform bfs here, no need dijkstra
        distance = 0
        while q2:
            for _ in range(len(q2)):
                row, col = q2.popleft()
                for drow, dcol in directions: 
                    if 0 <= drow+row < n and 0 <= dcol + col < n:
                        if grid[drow+row][dcol+col] == 1:
                            return distance
                        elif grid[drow+row][dcol+col] == 0:
                            q2.append((drow+row, dcol+col))
                            grid[drow+row][dcol+col] = 2 # As a bfs reach this pos another time, it must be a longest path.
            distance += 1
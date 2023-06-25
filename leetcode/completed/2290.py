from typing import List
from collections import deque
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        q = deque()
        q.append([0,0,0])
              
        def isValidNeighbour(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == -1:
                return False
            return True

        while q:
            node = q.popleft()

            if node[0] == len(grid)-1 and node[1] == len(grid[0])-1:
                return node[2]

            if grid[node[0]][node[1]] == 1:
                node[2] += 1

            if grid[node[0]][node[1]] == -1:
                continue
            grid[node[0]][node[1]] = -1

            for drow, dcol in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_row, new_col = node[0]+drow, node[1]+dcol
                if isValidNeighbour(new_row, new_col):
                    if grid[new_row][new_col] == 1:
                        q.append([new_row, new_col, node[2]])
                    else:
                        q.appendleft([new_row, new_col, node[2]])
            # print(q)




sol = Solution()
print(sol.minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]))

# [
#     0,1,1
#     1,1,1
#     1,1,0
# ] 

# [0,0,0]
# [1,0,0], [0,1,0]
# [0,1,0], [1,1,1], [2,0,1]
# [1,1,1], [2,0,1], [0,2,1], [1,1,1]
# [2,0,1], [0,2,1], [1,1,1], [1,2,2], [2,1,2]


# deque() -> [row, col, step]
# keep track of visited nodes -> set grid[i][j] = -1
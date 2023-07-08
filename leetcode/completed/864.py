from typing import List
from heapq import heappop, heappush

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]
        heap = [] # (key_len, keys, steps, row, col)
        visited = set()

        total_key_len = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    start_row, start_col = i, j
                elif grid[i][j].isalpha() and grid[i][j].islower():
                    total_key_len += 1

        heappush(heap, (0, 0, '', start_row, start_col))

        while heap:
            step, key_len, key, row, col = heappop(heap)
            # print(heap)
            # print(f"row:{row}, col:{col}, key:{key}, step:{step}")
            if (row, col, key) in visited:
                continue
            visited.add((row, col, key))
            if key_len == -total_key_len:
                return step
            for drow, dcol in directions:
                if 0 <= row+drow < n and 0 <= col+dcol < m and grid[row+drow][col+dcol] != '#' and (row+drow, col+dcol) not in visited:
                    cur_grid = grid[row+drow][col+dcol] 
                    if cur_grid.isalpha():
                        if cur_grid.isupper():
                            if cur_grid.lower() in key:
                                heappush(heap, (step+1, key_len, key, row+drow, col+dcol))
                        else:
                            if cur_grid in key:
                                heappush(heap, (step+1, key_len, key, row+drow, col+dcol))
                            else:
                                heappush(heap, (step+1, key_len-1, key+cur_grid, row+drow, col+dcol))
                    elif cur_grid in '@.':
                        heappush(heap, (step+1, key_len, key, row+drow, col+dcol))

        return -1


sol = Solution()
print(sol.shortestPathAllKeys(["@abcdeABCDEFf"]))
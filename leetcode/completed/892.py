from typing import List
class Solution: # didnt see row_len == col_len, this works if row_len != col_len?
    def surfaceArea(self, grid: List[List[int]]) -> int:
        row_len, col_len = len(grid), len(grid[0])
        area = 0
        # if grid is 1D:
        if row_len == 1 and col_len == 1:
            return 2 + (grid[0][0])*4
        
        # bottom and top:
        area += row_len * col_len * 2

        # deduct grid of 0:
        for g in grid:
            area -= g.count(0) * 2

        # outer surface other than bottom and top:
        for i in range(row_len):
            for j in range(col_len):
                if (i>0 and i<row_len-1) and (j>0 and j<col_len-1):
                    continue
                # corner
                if ((i==0 and j == 0) or (i==row_len-1 and j == 0) or (i==0 and j == col_len-1) or (i==row_len-1 and j == col_len-1)):
                    area += grid[i][j] * 2
                    print(grid[i][j] * 2)
                else:
                    area += grid[i][j]
                    print(grid[i][j])

        def isValid(row, col):
            if row < 0 or row >= row_len or col < 0 or col >= col_len:
                return False
            return True

        # inner surface
        for row in range(row_len):
            for col in range(col_len):
                for drow, dcol in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if isValid(row+drow, col+dcol) and grid[row+drow][col+dcol] > grid[row][col]:
                        area += grid[row+drow][col+dcol] - grid[row][col]

        return area                       

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        
        l = len(grid)
        area=0
        for row in range(l):
            for col in range(l):
                if grid[row][col]:
                    area += (grid[row][col]*4) +2 #surface area of each block if blocks werent connected
                if row: #row>0
                    area -= min(grid[row][col],grid[row-1][col])*2 #subtracting as area is common among two blocks
                if col: #col>0
                    area -= min(grid[row][col],grid[row][col-1])*2 #subtracting as area is common among two blocks
        return area

sol = Solution()
print(sol.surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))
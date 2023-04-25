class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        maxR , maxC = len(grid) , len(grid[0])

        self.maximum = 0

        def dfs(grid, row, col, det):
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"

            if row - 1 >= 0:
                dfs(grid, row - 1, col, False)
            if row + 1 < maxR:
                dfs(grid, row + 1, col, False)
            if col - 1 >= 0:
                dfs(grid, row, col - 1, False)
            if col + 1 < maxC:
                dfs(grid, row, col + 1, False)

            if det:
                self.maximum += 1

        for row in range(maxR):
            for col in range(maxC):
                dfs(grid, row, col, True)
                
        return self.maximum


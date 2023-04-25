class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        self.maxR, self.maxC = len(grid), len(grid[0])
        self.largest = 0
        self.cumulative = 0
        for row in range(self.maxR):
            for col in range(self.maxC):
                self.cumulative = 0
                self.dfs(grid, row, col)
        return self.largest
    
    def dfs(self, grid, r, c):
        if grid[r][c] == 1:
            grid[r][c] = 0
            self.cumulative += 1
            if r-1 >= 0:
                self.dfs(grid, r-1, c)
            if r+1 < self.maxR:
                self.dfs(grid, r+1 ,c)
            if c+1 < self.maxC:
                self.dfs(grid, r, c+1)
            if c-1 >= 0:
                self.dfs(grid, r, c-1)
            self.largest = max(self.largest, self.cumulative)
        
            

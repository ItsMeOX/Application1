class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 for _ in range(n)] for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                grid[row][col] = grid[row-1][col] + grid[row][col-1]

        return grid[m-1][n-1]

sol = Solution()
print(sol.uniquePaths(5,5))
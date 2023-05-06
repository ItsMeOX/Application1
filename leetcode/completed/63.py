class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        for i in range(len(obstacleGrid)): # flip grid
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = 1
                else:
                    obstacleGrid[i][j] = 0

        for i in range(1, len(obstacleGrid[0])): # for horizontal, if i - 1 is obstacle, i is also obstacle
            if obstacleGrid[0][i-1] == 0:
                obstacleGrid[0][i] = 0
        for i in range(1,len(obstacleGrid)): # same for vertical
            if obstacleGrid[i-1][0] == 0:
                obstacleGrid[i][0] = 0
        for i in range(1,len(obstacleGrid)): # start at (1,1) and count total possible paths
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j]:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]

        return obstacleGrid[-1][-1]

sol = Solution()
print(sol.uniquePathsWithObstacles([[0,0],[0,0]]))


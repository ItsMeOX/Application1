class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = [[0,grid[0].index(2)]]
        maxR, maxC = len(grid), len(grid[0])
        ct,ct2 = 1 , 0
        res = 0
        
        while q:
            for _ in range(ct):
                y,x = q.pop(0)
                grid[y][x] = 2
                for dy, dx in [[-1,0],[1,0],[0,-1],[0,1]]:
                    new_y = y + dy
                    new_x = x + dx
                    if new_y >= 0 and new_y < maxR and new_x >= 0 and new_x < maxC and grid[new_y][new_x] == 1:
                        q.append([new_y,new_x])
                        ct2 += 1
            ct = ct2
            ct2 = 0
            res += 1

        for r in grid:
            for c in r:
                if c == 1:
                    return -1
        return res - 1

grid = [[2,1,1],[0,1,1],[1,0,1]]
sol = Solution()
print(sol.orangesRotting(grid))
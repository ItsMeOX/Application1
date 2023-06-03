from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        
        l = len(grid)
        q = deque([(0,0)])
        visited = {(0,0)}
        steps = 1

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()

                if row == l - 1 and col == l - 1:
                    return steps

                for drow in range(-1,2):
                    for dcol in range(-1,2):
                        if (drow or dcol) and (-1<drow+row<l) and (-1<dcol+col<l) and not grid[drow+row][dcol+col] and (drow+row, dcol+col) not in visited:
                            q.append((drow+row, dcol+col))
                            visited.add((drow+row, dcol+col))
            steps += 1

        return -1

sol = Solution()
print(sol.shortestPathBinaryMatrix([[0,1],[1,0]]))
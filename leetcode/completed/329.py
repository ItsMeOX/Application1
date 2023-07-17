from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}

        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]

            cur_longest = 0
            for dr, dc in directions:
                new_r, new_c = row+dr, col+dc
                if 0 <= new_r < m and 0 <= new_c < n and matrix[new_r][new_c] > matrix[row][col]:
                    cur_longest = max(cur_longest, dfs(new_r, new_c))
            
            memo[(row, col)] = cur_longest + 1
            return cur_longest + 1

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        res = 0
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            for col in range(n):
                res = max(res, dfs(row, col))

        return res

sol = Solution()
print(sol.longestIncreasingPath([
    [10,19,5,16,3],
    [10,13,4,8,15],
    [5,12,9,15,19],
    [2,10,17,13,16],
    [3,4,11,15,12],
    [3,10,1,5,17],
    [12,17,8,4,9]
]))
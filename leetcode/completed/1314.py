from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        prefix = [[0]*(n+1) for _ in range(m+1)]

        for r in range(1, m+1):
            for c in range(1, n+1):
                prefix[r][c] = prefix[r-1][c] + prefix[r][c-1] + mat[r-1][c-1] - prefix[r-1][c-1]

        res = [[0]*n for _ in range(m)]

        for r in range(1, m+1):
            for c in range(1, n+1):
                res[r-1][c-1] = prefix[min(m, r+k)][min(n, c+k)] - prefix[min(m, r+k)][max(0, c-k-1)] - prefix[max(0, r-k-1)][min(n, c+k)] + prefix[max(0, r-k-1)][max(0, c-k-1)]

        return res
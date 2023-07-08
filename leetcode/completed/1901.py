from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]: # O( rlen * clen )
        r, c = 0, 0
        rlen, clen = len(mat), len(mat[0])
        while True:
            if c + 1 != clen and mat[r][c+1] > mat[r][c]:
                c += 1
            elif c > 0 and mat[r][c-1] > mat[r][c]:
                c += -1
            elif r > 0 and mat[r-1][c] > mat[r][c]:
                r += -1
            elif r + 1 != rlen and mat[r+1][c] > mat[r][c]:
                r += 1
            else:
                return [r, c]


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]: # O( rlen * log(clen) )
        left, right = 0, len(mat[0])-1
        while left <= right:
            m = (left+right) // 2
            maxRow = 0

            for j in range(len(mat)):
                if mat[j][m] > mat[maxRow][m]:
                    maxRow = j
            
            rightLarger = m+1 < len(mat[0]) and mat[maxRow][m+1] > mat[maxRow][m]
            leftLarger  = m-1 >= 0 and mat[maxRow][m-1] > mat[maxRow][m]

            if leftLarger:
                right = m - 1
            elif rightLarger:
                left = m + 1
            else:
                return [maxRow, m]
            
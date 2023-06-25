from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        col = len(mat[0])
        row = len(mat)

        if row*col != r*c:
            return mat

        res = []
        temp = []
        cur_c = 0
        cur_r = 0
        temp_len = 0
        for _ in range(r*c):
            temp.append(mat[cur_r][cur_c])
            cur_c += 1
            temp_len += 1
            if cur_c == col:
                cur_c = 0
                cur_r += 1
            if temp_len == c:
                temp_len = 0
                res.append(temp)
                temp = []          

        return res
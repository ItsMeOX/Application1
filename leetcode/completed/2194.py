from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        res = []
        rowStart, rowEnd = alpha.index(s[0]), alpha.index(s[3])
        colStart, colEnd = int(s[1]), int(s[4])

        for i in range(rowStart, rowEnd+1):
            cur_alpha = alpha[i]
            for j in range(colStart, colEnd+1):
                res.append(f"{cur_alpha}{j}")

        return res
        
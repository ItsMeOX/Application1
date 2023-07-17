from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        special = set()
        forbidden = set()

        for row in range(len(mat)):
            temp = []
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    temp.append(col)
            for t in temp:
                if t in special:
                    special.remove(t)
                elif len(temp) == 1 and t not in forbidden:
                    special.add(t)
                forbidden.add(t)

        return len(special)
    
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        transpose = [i for i in zip(*mat)]
        res = 0

        for row in mat:
            if row.count(1) == 1:
                idx = row.index(1)

                if transpose[idx].count(1) == 1:
                    res += 1

        return res
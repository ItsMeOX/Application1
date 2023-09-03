from typing import List

# We start from top left corner (r = c = 0).
# Notice that our directions will always be right -> bottom -> left -> up.
# So, we initialize a 'directions' tuple which stores (dr, dc), and the order of these directions will be the order stated above.
# Then we iterate from i = 1 to i = n^2.
# Every time we walk out of bound from our array or every time we meet a position that already contains number, we change our direction.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        i = 1
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0)) # r, d, l, u
        direction_idx = 0
        r = c = 0
        res = [[0]*n for _ in range(n)]

        while i <= n*n:
            res[r][c] = i
            dr, dc = directions[direction_idx]
            if r+dr < 0 or r+dr >= n or c < 0 or c+dc >= n or res[r+dr][c+dc]:
                direction_idx += 1
                direction_idx %= 4
            dr, dc = directions[direction_idx]
            r = r+dr
            c = c+dc
            i += 1
        
        return res
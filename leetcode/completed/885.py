from typing import List

# steps & steps_change: if steps == steps_change: we have to change direction
# steps_change2: every time after changing direction twice, steps_change has to increase by 1, so steps_change2 keeps track when to increase steps_change by 1.

# If (r, c) is in valid grid, then append (r, c) to res until len(res) == rows * col.

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0)) # right, down, left, top
        direction_index = 0
        steps = steps_change2 = 0
        steps_change = 1
        r, c = rStart, cStart
        res = []

        while len(res) < rows * cols:
            if 0 <= r < rows and 0 <= c < cols:
                res.append([r, c])
            if steps == steps_change:
                steps = 0
                direction_index = (direction_index + 1)%4
                steps_change2 += 1
                if steps_change2 == 2:
                    steps_change2 = 0
                    steps_change += 1
            dr, dc = directions[direction_index]
            r += dr
            c += dc

            steps += 1

        return res
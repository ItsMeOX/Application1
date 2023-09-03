from typing import List

# generate all the coordinates and sort them by the distance from (rCenter, cCenter).

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        return sorted(([row, col] for row in range(rows) for col in range(cols)), key = lambda x: abs(rCenter-x[0]) + abs(cCenter-x[1]))
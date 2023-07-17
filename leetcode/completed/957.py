from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        for _ in range((n-1)%14+1):
            cells_copy = cells.copy()
            for i in range(1, len(cells)-1):
                if cells_copy[i-1] == cells_copy[i+1]:
                    cells[i] = 1
                else:
                    cells[i] = 0
            cells[0] = cells[-1] = 0
        return cells

sol = Solution()
print(sol.prisonAfterNDays(cells = [1,0,0,1,0,0,1,0], n = 100))
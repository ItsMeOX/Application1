import math
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        return [math.comb(rowIndex, i) for i in range(rowIndex+1)]        



sol = Solution()
print(sol.getRow(3))
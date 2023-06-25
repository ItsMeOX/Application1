from typing import List
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        res = 0

        # bottom to first special
        res = special[0] - bottom

        # between specials
        for i in range(1, len(special)):
            res = max(res, special[i]-special[i-1]-1)

        # last speical to top
        res = max(res, top - special[-1])
        
        return res

sol = Solution()
print(sol.maxConsecutive(bottom = 6, top = 8, special = [7,6,8]))
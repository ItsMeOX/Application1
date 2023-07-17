from typing import List
from math import ceil
from bisect import bisect_right

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        spell_needed = [ceil(success/i) for i in potions]
        prefix_sum = {}

        for s in spell_needed:
            prefix_sum[s] = prefix_sum.get(s, 0) + 1

        sorted_key = sorted(prefix_sum.keys())

        for i in range(1, len(sorted_key)):
            prefix_sum[sorted_key[i]] += prefix_sum[sorted_key[i-1]]
        
        res = []
        for spell in spells:
            idx = bisect_right(sorted_key, spell)-1
            key = sorted_key[idx]
            if idx == -1:
                res.append(0)
            else:
                res.append(prefix_sum[key])

        return res

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for spell in spells:
            lo, hi = 0, len(potions)-1
            while lo <= hi:
                m = (lo+hi) // 2
                if potions[m] * spell >= success:
                    hi = m - 1
                else:
                    lo = m + 1
            
            if lo == len(potions):
                res.append(0)
            else:
                res.append(len(potions)-lo)
        
        return res

sol = Solution()
print(sol.successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7))
print(sol.successfulPairs(spells = [3,1,2], potions = [8,5,8], success = 16))
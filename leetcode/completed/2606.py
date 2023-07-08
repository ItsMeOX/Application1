from typing import List

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        cost = {}
        for i, c in enumerate('abcdefghijklmnopqrstuvwxyz'):
            cost[c] = i + 1
        for i in range(len(chars)):
            cost[chars[i]] = vals[i]
        
        res = 0
        temp = 0
        for c in s:
            temp += cost[c]
            res = max(res, temp)
            if temp < 0:
                temp = 0

        return res
        
sol = Solution()
print(sol.maximumCostSubstring(s = "adaa", chars = "d", vals = [-1000]))
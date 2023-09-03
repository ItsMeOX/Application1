from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        right = 0
        res = 0
        for i in range(len(g)):
            while right < len(s) and s[right] < g[i]:
                right += 1
            if right == len(s):
                break
            res += 1
            right += 1

        return res
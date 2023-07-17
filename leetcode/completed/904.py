from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        cnt = 0
        seen = defaultdict(int)
        res = 0

        for fruit in fruits:
            seen[fruit] += 1
            cnt += 1
            while len(seen) > 2:
                seen[fruits[left]] -= 1
                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]
                left += 1
                cnt -= 1
            res = max(res, cnt)

        return res
from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = bank[0].count('1')

        for i in range(1, len(bank)):
            cur = bank[i].count('1')
            if cur:
                res += prev * cur
                prev = cur

        return res
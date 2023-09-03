from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set()
        res = 0

        for word in words:
            if word in seen:
                res += 1
            else:
                seen.add(word[::-1])

        return res
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = {}

        for num in arr:
            cnt[num] = cnt.get(num, 0) + 1

        return len(cnt.values()) == len(set(cnt.values()))
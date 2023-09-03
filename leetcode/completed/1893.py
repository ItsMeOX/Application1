from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        not_covered = set(i for i in range(left, right+1))

        for start, end in ranges:
            for i in range(start, end+1):
                if i in not_covered:
                    not_covered.remove(i)
        
        return not not_covered
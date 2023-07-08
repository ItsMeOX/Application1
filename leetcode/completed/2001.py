from typing import List

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        cnt = {}
        res = 0

        for w, h in rectangles:
            ratio = w/h
            if ratio in cnt:
                res += cnt[ratio]
            cnt[ratio] = cnt.get(ratio, 0) + 1

        return res
from typing import List

# Because that the res array will be like [True, True, True, ..., True, False, False, ...],
# so we can use binary search to solve this.
# We set the lower boundary to be 0, higher boundary to length to removable.
# For every 'm', we check from removable[0] to removable[m],
# 1. if after removals and p is still subsequence of s, then increase lower bound.
# 2. if after removals and p is not more subsequence of s, then decrease higher bound as we have removed letters that are needed for p to be subsequence of s.

# When lo=0, hi=1, we will check if removable[0] is removable or not, 
# if not then final answer will be 0,
# if yes then final answer will be 1.


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        lo, hi = 0, len(removable)

        def check(i):
            skips = set(removable[:i+1])
            ptr = 0
            for i in range(len(s)):
                if i in skips:
                    continue
                if s[i] == p[ptr]:
                    ptr += 1
                if ptr == len(p): 
                    return True

            return False

        while lo < hi:
            m = (lo+hi) // 2
            if check(m):
                lo = m + 1
            else:
                hi = m

        return lo
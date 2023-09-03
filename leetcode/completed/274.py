from typing import List

# Here we apply binary search just like the 'coco eats banana' questions.
# Set lower bound to 0, upper bound to length of citations + 1. ( citations + 1 here because our binary search is [low, high) )
# We initialize a helper function 'check', which loop through the 'citations' list and count how many citation are > k. ( k here is the m of binary search )
# If the citation count is >= than k, we raise our k as there might be value larger than k that is still valid.
# Else, we decrease k until we find a number that is valid.
# At last, we need to -1 because we increased lo to lo+1 when m is valid.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def check(k):
            cnt = 0
            for c in citations:
                if c >= k:
                    cnt += 1

            return cnt

        lo, hi = 0, len(citations)+1

        while lo < hi:
            m = (lo+hi) // 2
            if check(m) >= m:
                lo = m + 1
            else:
                hi = m

        return lo - 1
    
# There is another approach using sorting that is unintuitive atleast for me.
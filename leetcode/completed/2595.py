from typing import List

# Note that,
# for 0th indexed array,
# the last element will always be even, 
# the second last element will always be odd,
# ...

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = odds = cnt = 0
        while n:
            if n & 1:
                if cnt & 1:
                    odds += 1
                else:
                    even += 1
            cnt += 1
            n >>= 1

        return [even, odds]
from typing import List

# Perform binary search here, 
# the lower bound will be 1, which means splitting the whole array to [1,1,1,...]
# the upper bound will be max(nums), which means not splitting any number.
# For every m, we check how many operations are needed to split the array into numbers <= m,
# if the operations needed are > maxOperations, then we need to lower the number for array to be splitted to.
# if the operations needed are <= maxOperations, then that will be the answer, so hi = m.

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        lo, hi = 1, max(nums)

        def check(x):
            ops = 0
            for num in nums:
                ops += (num-1) // x
                if ops > maxOperations:
                    return False
            return True

        while lo < hi:
            m = (lo+hi) // 2

            if check(m):
                hi = m
            else:
                lo = m + 1
        
        return lo
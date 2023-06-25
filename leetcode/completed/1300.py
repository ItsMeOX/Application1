from typing import List
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        lo, hi = 0, max(arr)

        def check(num):
            sum_ = 0
            for n in arr:
                if n > num:
                    sum_ += num
                else:
                    sum_ += n
            return sum_

        while lo < hi:
            m = (lo+hi) // 2

            if abs(target - check(m)) <= abs(target - check(m+1)):
                hi = m 
            else:
                lo = m + 1

        return lo

sol = Solution()
print(sol.findBestValue(arr = [4,9,3], target = 10))
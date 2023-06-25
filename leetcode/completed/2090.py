from typing import List
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        res = []

        _sum = sum(nums[:2*k+1])
        first_idx = 0

        for i in range(l):
            if i < k or i > l - k - 1 :
                res.append(-1)
            else:
                res.append(_sum // (2*k+1))
                _sum -= nums[first_idx]
                first_idx += 1
                if i + k + 1 < l:
                    _sum += nums[i+k+1]
        return res

from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one = -1
        for i in range(len(nums)):
            if nums[i]:
                if last_one != -1 and i - last_one - 1 < k:
                    return False
                last_one = i
        return True
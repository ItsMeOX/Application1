from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counter = {}
        for row in nums:
            for num in row:
                counter[num] = counter.get(num, 0) + 1

        res = []
        for key in counter:
            if counter[key] >= len(nums):
                res.append(key)

        return sorted(res)
    
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        seen = set(nums[0])

        for num in nums:
            seen = seen & set(num)

        return sorted(seen)
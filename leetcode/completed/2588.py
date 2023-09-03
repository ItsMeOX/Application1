from typing import List

# For subarray to be valid, every digit in binary form of all numbers in that subarray 
# must XOR to 0.
# For example: [3, 1, 2]
# 3    1    2
# 11   01   10
# 3^1^2 = 0.

# Every time we XOR cur to a seen cur in array,
# there will be valid subarray.

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        counter = {0: 1}
        cur = 0
        res = 0

        for num in nums:
            cur ^= num
            if cur in counter:
                res += counter[cur]
            counter[cur] = counter.get(cur, 0) + 1
        
        return res
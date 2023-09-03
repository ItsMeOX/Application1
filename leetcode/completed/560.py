from typing import List

# [1,1,1], k = 2,

# i = 0,
# counter = {0:1}
# cur_sum = 1
# cur_sum - k = 1 - 2 = -1 not in counter

# i = 1,
# counter = {0:1, 1:1}
# cur_sum = 2
# 2 - 2 = 0 in counter, res += 1

# i = 2,
# counter = {0:1, 1:1, 2:1}
# cur_sum = 3
# 3 - 2 = 1 in counter, res += 1 

# i = 3,
# counter = {0:1, 1:1, 2:1, 3:1}

# if all number in nums are positive (0, +inf), then we do not need to count how many time the prefix sum has appeared.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = {0: 1}
        cur_sum = 0
        res = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum - k in counter:
                res += counter[cur_sum - k]
            counter[cur_sum] = counter.get(cur_sum, 0) + 1
        
        return res
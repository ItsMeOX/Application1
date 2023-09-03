from typing import List


# For every i from 0 to len(s),
# if i is odd, res[i] = odd sum before i + even sum after i
# if i is even, res[i] = even sum before i + odd sum after i

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        cu = [0, 0]
        for i in range(2, len(nums)+2):
            cu.append(nums[i-2] + cu[i-2])

        total_even = sum(nums[::2])
        total_odd = sum(nums[1::2])

        res = 0        
        for i in range(2, len(nums)+2):
            if i & 1:
                odd = cu[i-2] + total_even - cu[i-1]
                even = cu[i-1] + total_odd - cu[i]
            else:
                odd = cu[i-1] + total_even - cu[i]
                even = cu[i-2] + total_odd - cu[i-1]

            if odd == even: res += 1

        return res
    

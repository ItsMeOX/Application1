from typing import List

# Variant of sum of subarray == target.
# Use the prefix sum technique, if we get sum(subarray) == target, we will reset the prefix so we cannot reuse this subarray.

# Cannot use two pointers here because of for example: [-5, 5], target = 5.

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefix = set()
        sums = 0
        res = 0

        for num in nums:
            sums += num
            if sums - target in prefix or sums - target == 0:
                sums = 0
                prefix = set()
                res += 1
            else:
                prefix.add(sums)


        return res
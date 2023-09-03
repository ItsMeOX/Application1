from typing import List

# No need to sort array here,
# we just need to calculate the amount of numbers < target (pre),
# and the amount of numbers == target (cnt).
# Then we create the res array which contains index from 'pre' to 'pre+cnt-1'.

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        pre = 0
        cnt = 0
        for n in nums:
            if n == target:
                cnt += 1
            elif n < target:
                pre += 1
        
        return [i for i in range(pre, pre + cnt)]
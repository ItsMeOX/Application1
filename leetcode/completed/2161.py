from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        after = []
        pivot_cnt = 0

        for num in nums:
            if num < pivot:
                before.append(num)
            elif num > pivot:
                after.append(num)
            else:
                pivot_cnt += 1
        
        return before + [pivot] * pivot_cnt + after
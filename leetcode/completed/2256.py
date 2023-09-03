from typing import List

# Utilize prefix sum here, 
# Avg at index i = ( sum_left / len_left - sum_right / len_right ).
# If avg at index i < smallest avg (best) then update best index and best.

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        best_index = 0
        best = float('inf')
        right = sum(nums)
        left = 0
        n = len(nums)

        for i in range(len(nums)):
            left += nums[i]
            right -= nums[i]
            left_n = i + 1
            right_n = n - i - 1 or 1 # prevent division by zero.
            res = abs(left//left_n - right//right_n)
            if res < best:
                best = res
                best_index = i
            if best == 0: # little optimization here: if best == 0, the global best must be 0 as abs cannot be < 0.
                return best_index
        
        return best_index
            

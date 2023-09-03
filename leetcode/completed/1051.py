from typing import List

# Initialize counter where counter[i] is the frequency of i in heights.
# Then iterate through 'heights', 
# If counter[ptr] == 0, keep increasing ptr until we counter[ptr] > 0.
# Compare counter[ptr] with current height,
# if it is not same the increase 'res',
# then decrease count of counter[i] by 1.

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = [0] * (max(heights)+1)

        for h in heights:
            counter[h] += 1
        
        res = 0
        ptr = 0
        for h in heights:
            while counter[ptr] == 0:
                ptr += 1
            if h != ptr:
                res += 1
            counter[ptr] -= 1

        return res 
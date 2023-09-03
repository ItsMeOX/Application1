from typing import List

# Sort the 'nums' list from smallest to largest.
# Initialize the 'smallest' var which is the current smallest number to first number in nums.
# Initialize the 'delta' var which is the current amount of operation needed to reduce number to the smallest number in 'nums'.
# Initiliaze the 'res' var which is the total amount of operation needed to reduce number to the smallest number in 'nums'.
# Iterate through the sorted 'nums' list.
# If current number is larger than current smallest number, increase delta by one as it will take 1 more operation to reduce it to the smallest, 
# also set smallest to current number.
# If current number is the same as smallest number, then we just add delta ( n. of operation needed to reduce current num to smallest ) to res.
# The final res will be our answer.

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        delta = 0
        smallest = nums[0]

        for num in nums:
            if num > smallest:
                smallest = num
                delta += 1
            res += delta
            
        return res
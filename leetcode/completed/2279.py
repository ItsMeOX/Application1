from typing import List

# Create a sorted array which stores the remaining capacity for each bag in increasing order.
# Then, greedily fill additional rocks into bags which current capacity remaining is the least.
# For each bag filled, add 1 to res.
# If addtional rocks cannot fully fill capacity of current bag, break the loop.
# Final res will be our answer.

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        capacityLeft = sorted(capacity[i]-rocks[i] for i in range(n))

        res = 0

        for i in range(n):
            if additionalRocks < capacityLeft[i]:
                break
            res += 1
            additionalRocks -= capacityLeft[i]

        return res
from typing import List

# We initialize 'res' as a list of initial value of [0, 0, 0].
# Iterate through triplets array and if all the values of triplets array are smaller than target,
# We greedily get the max value between that current triplet and res array.
# Finally, if all the values in res is the same as target, we return true,
# otherwise return false.

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]

        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                res[0] = max(res[0], x)
                res[1] = max(res[1], y)
                res[2] = max(res[2], z)
                if res == target:
                    return True
        
        return res == target
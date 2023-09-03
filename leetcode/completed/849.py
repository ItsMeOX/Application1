from typing import List

# 'left' variable is the idx of last occupied seat, set 'left' to -1 initially indicating no occupied seat found yet.
# Iterate i from 0 to length-1 of 'seats' array, and if current seat is occupied:
# 1. if left is -1, that means it will be [0 0 1 ...], so update 'res' with 'i'.
# 2. if left was found before, then we take the middle seat from last 'left' to current index, and determine the distance from 'middle' to 'left'. 
#    if n. of seats between are odds: [1 0 0 0 1], then the distance will be 2 - 0 = 2.
#    if n. of seats between are even: [1 0 0 0 0 1], as we round down our middle index, so it will be closer to 'left', 2 - 0 = 2.
#                                                                                       (we also want shorter distance.)
# then we update left with current index.
# For the case like [1 0 0 0], we can check for this case by len(seats) - left - 1.

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = -1
        res = 1

        for i in range(len(seats)):
            if seats[i]:
                if left == -1:
                    res = max(res, i)
                else:
                    res = max(res, (i+left)//2 - left)
                left = i

        return max(res, len(seats)-left-1)
from typing import List
from bisect import bisect_left
from random import randint

# Initialize a prefix sum for w,
# if w = [1,3,5],
# then prefix_sum = [1, 4, 9] ([1-1, 2-4, 5-9]).
# When picking, random choose a number between 1 ~ prefix_sum[-1],
# then use binary search to search which index it belongs to.
# Note that we have to choose from 1 ~ prefix[-1], not 0 ~ prefix[-1].

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [w[0]]
        for i in range(1, len(w)):
            self.prefix.append(self.prefix[-1]+w[i])

    def pickIndex(self) -> int:
        rand_idx = randint(1, self.prefix[-1])
        return bisect_left(self.prefix, rand_idx)        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
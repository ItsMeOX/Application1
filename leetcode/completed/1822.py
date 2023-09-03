from typing import List
from functools import reduce

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = reduce(lambda a, b: a*b, nums)
        
        return -1 if product < 0 else 1 if product > 0 else 0
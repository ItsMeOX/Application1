from typing import List
from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = defaultdict(int)
        for row in matrix:
            counter[tuple(row)] += 1
            inverse = [1 - elm for elm in row]
            counter[tuple(inverse)] += 1
        
        return max(counter.values())
from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1 or k == len(weights): return 0
        scores = sorted([weights[i]+weights[i+1]+weights[0]+weights[-1] for i in range(len(weights)-1)])

        res = 0
        for i in range(k-1):
            res += scores[len(scores) -1 - i] - scores[i]

        return res
    
sol = Solution()
print(sol.putMarbles(weights = [1,3], k = 2))
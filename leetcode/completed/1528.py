from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0] * len(s)

        for i in range(len(indices)):
            res[indices[i]] = s[i]
        
        return ''.join(res)
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j-1][i] > strs[j][i]:
                    res += 1
                    break
        
        return res
    
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(col != sorted(col) for col in map(list, zip(*strs)))
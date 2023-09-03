from typing import List

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = 0
        for w in strs:
            isdigit = True
            for c in w:
                if c.isalpha():
                    isdigit = False
                    break
            if isdigit:
                res = max(res, int(w))
            else:
                res = max(res, len(w))
        
        return res
    
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = 0
        for w in strs:
            if w.isdigit():
                res = max(res, int(w))
            else:
                res = max(res, len(w))
        
        return res
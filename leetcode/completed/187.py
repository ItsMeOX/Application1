from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = {}
        res = []
        for i in range(10, len(s)+1):
            cur_str = s[i-10:i]
            if cur_str in seen and seen[cur_str] == 1:
                res.append(cur_str)
            seen[cur_str] = seen.get(cur_str, 0) + 1
        
        return res
    
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        for i in range(10, len(s)+1):
            cur_str = s[i-10:i]
            if cur_str in seen:
                res.add(cur_str)
            seen.add(cur_str)
        
        return list(res)
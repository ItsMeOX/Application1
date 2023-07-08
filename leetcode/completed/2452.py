from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        
        for qword in queries:
            for dword in dictionary:
                cnt = 0
                for i in range(len(qword)):
                    if qword[i] != dword[i]:
                        cnt += 1
                    if cnt > 2:
                        break
                if cnt <= 2:
                    res.append(qword)
                    break
        return res
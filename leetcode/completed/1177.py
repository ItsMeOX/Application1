from typing import List

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        count = [[0]*26]

        for i in range(len(s)):
            temp = count[-1].copy()
            temp[ord(s[i]) - ord('a')] += 1
            count.append(temp)
        
        res = []
        for left, right, x in queries:
            single = 0
            for i in range(26):
                if ( count[right+1][i] - count[left][i] ) & 1:
                    single += 1
            if single <= 1:
                res.append(True) 
            else:
                if single & 1: # can only write single // 2 <= x
                    res.append((single-1)//2 <= x)
                else:
                    res.append(single//2 <= x)

        return res                    
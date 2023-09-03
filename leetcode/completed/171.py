
# Example:
#    A       A        A        A
# 26^3*1 + 26^2*1 + 26^1*1 + 26^0*1
# = 26^n * (ord(text[i])-ord('A')+1) 
# n = 0th index from back, last element is 0, second last element is 1.
# i = ith from front, first element is 0, second element is 1.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0

        for i in range(len(columnTitle)-1, -1, -1):
            res += 26**(len(columnTitle)-i-1) * (ord(columnTitle[i])-ord('A')+1)


        return res
    
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        factor = 1

        for i in range(len(columnTitle)-1, -1, -1):
            res += factor * (ord(columnTitle[i])-ord('A')+1)
            factor *= 26

        return res
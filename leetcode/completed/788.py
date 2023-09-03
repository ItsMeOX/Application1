class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        mapper = {'2':'5', '5':'2', '6':'9', '9':'6'}
        for i in range(1, n+1):
            temp = str(i)
            new = ''
            if '3' in temp or '4' in temp or '7' in temp: continue
            for c in temp:
                if c in mapper:
                    temp += mapper[c]                    
                else:
                    new += c
            
            if new != temp:
                res += 1

        return res
    

class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0

        for i in range(1, n+1):
            temp = str(i)
            if '3' in temp or '4' in temp or '7' in temp: continue
            if '2' in temp or '5' in temp or '6' in temp or '9' in temp: res += 1

        return res
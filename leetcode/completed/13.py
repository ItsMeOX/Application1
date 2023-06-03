class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0
        idx = 0
        while idx < len(s):
            if idx < len(s)-1 and values[s[idx]] < values[s[idx+1]]:
                res += values[s[idx+1]] - values[s[idx]]
                idx += 1
            else:
                res += values[s[idx]]
            idx += 1

        return res
    

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0
        for i in range(len(s)-1):
            if values[s[i+1]] > values[s[i]]:
                res -= values[s[i]]
            else:
                res += values[s[i]]


        return res + values[s[-1]]
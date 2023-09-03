class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ''

        for i in range(len(s)):
            if i > 1 and res[-2] == res[-1] == s[i]:
                continue
            res += s[i]
        
        return res
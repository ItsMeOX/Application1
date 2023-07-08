class Solution:
    def minLength(self, s: str) -> int:
        hasSub = True
        while hasSub:
            if len(s) < 2: return len(s)

            for i in range(1, len(s)):
                if s[i-1:i+1] == 'AB' or s[i-1:i+1] == 'CD':
                    s = s[:i-1] + s[i+1:] 
                    break
                if i == len(s)-1:
                    hasSub = False

        return len(s)
    

class Solution:
    def minLength(self, s: str) -> int:
        while 'AB' in s or 'CD' in s:
            s = s.replace('AB', '').replace('CD', '')

        return len(s)
    
class Solution:
    def minLength(self, s: str) -> int:
        stk = []

        for c in s:
            if stk and stk[-1] + c in ('AB', 'CD'):
                stk.pop()
            else:
                stk.append(c)

        return len(stk)



sol = Solution()
print(sol.minLength(s = "ABFCACDB"))
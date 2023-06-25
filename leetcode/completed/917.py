from collections import deque
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        q = deque()
        res = ""
        for c in s:
            if c.isalpha():
                q.append(c)
        
        for i in range(len(s)):
            if s[i].isalpha():
                res += q.pop()
            else:
                res += s[i]
            
        return res
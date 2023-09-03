class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stk = []
        n = len(part)

        for c in s:
            stk.append(c)

            while ''.join(stk[-n:]) == part:
                for _ in range(n):
                    stk.pop()

        return ''.join(stk)
    
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '', 1)
        
        return s
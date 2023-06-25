class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left, right = 0, 0
        for c in s:
            if c == t[right]:
                right += 1
            if right == len(t):
                return 0
        
        return len(t) - right
class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        res = 0

        for c in s:
            if c == '(':
                depth += 1
                res = max(res, depth)
            elif c == ')':
                depth -= 1
        
        return res
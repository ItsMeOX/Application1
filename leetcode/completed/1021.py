class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt = 0
        res = ''

        for c in s:
            if c == ')':
                cnt -= 1
            if cnt > 0:
                res += c
            if c == '(':
                cnt += 1

        return res
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []

        for c in s:
            if not stk or stk[-1] != c:
                stk.append(c)
            else:
                stk.pop()

        return ''.join(stk)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        for c in s:
            if c == '(':
                stack.append("")
            elif c == ')':
                last_str = stack.pop()[::-1]
                stack[-1] += last_str
            else:
                stack[-1] += c

        return stack[0]
    
sol = Solution()
print(sol.reverseParentheses("(ed(et(oc)ed)el)"))
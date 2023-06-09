from collections import deque
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        valid = [0] * len(s)
        left_p = deque()
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                left_p.append(i)
            elif left_p:
                valid[left_p.pop()] = 1
                valid[i] = 1
        
        temp = 0
        for v in valid:
            if v:
                temp += 1
            else:
                res = max(res, temp)
                temp = 0
        return max(res, temp)
                
sol = Solution()
print(sol.longestValidParentheses("(()"
))
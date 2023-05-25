class Solution:
    def isValid(self, s: str) -> bool:
        # q = []
        # for c in s:
        #     if c in ")]}":
        #         if not q or ((c == ')' and q.pop() != '(') or (c == ']' and q.pop() != '[') or (c == '}' and q.pop() != '{')):
        #             return False
        #     else:
        #         q.append(c)

        # return not q

            
        q = []
        pair = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in '([{':
                q.append(pair[c])
            elif q and c == q[-1]:
                q.pop()
            else:
                return False
            
        return not q


sol = Solution()
print(sol.isValid("[[]()[(])]"))
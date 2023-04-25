# class Solution:
#     def letterCasePermutation(self, s: str) -> list[str]:
#         def dfs(s, left):

#             for idx,letter in enumerate(s[left:]):

#                 if not letter.isalpha() or letter.isupper():
#                     continue
                
#                 temp_s = s
#                 s = s[:idx+left] + s[idx+left].upper() + s[idx+left+1:]
#                 res.append(s)
#                 dfs(s,idx+left+1)
#                 s = temp_s

#         res = [s.lower()]
#         dfs(s.lower(), 0)
#         return res

class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        def dfs(sub="", idx=0):
            if len(sub) == len(s):
                res.append(sub)
                return
            if s[idx].isalpha():
                dfs(sub + s[idx].swapcase(), idx + 1)
            dfs(sub + s[idx], idx + 1)

        res = []
        dfs()
        return res

sol = Solution()
ans = sol.letterCasePermutation(s = "A")
print(ans)
print(len(ans))

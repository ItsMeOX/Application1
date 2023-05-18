# class Solution:
#     def mostPoints(self, questions: list[list[int]]) -> int:
#         memo = [0] * len(questions)
#         def dp(i):
#             if i >= len(questions):
#                 return 0
            
#             if memo[i]:
#                 return memo[i]

#             memo[i] = max(dp(i+1), dp(1 + i + questions[i][1]))

#             return memo[i]
        

#         return dp(0)
    
class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        def dp(i):
            if i >= len(questions):
                return 0
            
            if not questions[i][1]:
                return questions[i][0]

            questions[i][0] = max(dp(i + 1), questions[i][0] + dp(questions[i][1] + i + 1)) # skip to next, or add next to current value
            questions[i][1] = 0

            return questions[i][0]
        

        return dp(0)

mat = [[1,1],[2,2],[3,3],[4,4],[5,5]]

sol = Solution()
print(sol.mostPoints(mat))
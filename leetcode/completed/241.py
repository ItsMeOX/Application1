from typing import List

# If we meet a operator (+, -, *), then divide expression into left and right substring excluding this operator.
# If there is no more operator (pure digits), then return the digit.
# For example, 2*3-4*5, i = -2,
#      (2*3-4)   *   (5)
#      /     \         \
# (2*3)-(4)  (2)*(3-4)  5
#  /    \     /    \    
# 5     4     2     -1

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def dfs(expression):
            if expression.isdigit():
                return [int(expression)]

            res = []
            for i in range(len(expression)):
                if expression[i] not in '*+-': continue
                left = dfs(expression[:i])
                right = dfs(expression[i+1:])
                ops = expression[i]
                for l in left:
                    for r in right:
                        if ops == '*':
                            res.append(l*r)
                        elif ops == '-':
                            res.append(l-r)
                        else:
                            res.append(l+r)
            return res
        
        return dfs(expression)

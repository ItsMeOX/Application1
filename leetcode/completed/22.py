from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def build(s, left, right):
            if left == right == n:
                res.append(s)
                return
            
            if left + right > n*2 or right > left:
                return

            build(s+'(', left+1, right)
            build(s+')', left, right+1)

        build('', 0, 0)

        return res

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def build(s, left, right):
            if right == n:
                res.append(s)
            else:
                if left < n:
                    build(s+'(', left+1, right)
                if right < left:
                    build(s+')', left, right+1)

        build('', 0, 0)

        return res
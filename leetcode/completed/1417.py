class Solution:
    def reformat(self, s: str) -> str:
        alpha = ""
        numeric = ""

        for c in s:
            if c.isalpha():
                alpha += c
            else:
                numeric += c
        
        if abs(len(alpha) - len(numeric)) > 1:
            return ""

        res = ""
        for i in range(max(len(alpha), len(numeric))):
            if len(alpha) > len(numeric):
                if i < len(alpha):
                    res += alpha[i]
                if i < len(numeric):
                    res += numeric[i]
            else:
                if i < len(numeric):
                    res += numeric[i]
                if i < len(alpha):
                    res += alpha[i]

        return res

class Solution:
    def reformat(self, s: str) -> str:
        alpha = []
        numeric = []

        for c in s:
            if c.isalpha():
                alpha.append(c)
            else:
                numeric.append(c)

        res = ""
        if abs(len(alpha) - len(numeric)) < 2:
            while alpha and numeric:
                res += alpha.pop()
                res += numeric.pop()
            if alpha:
                res = res + alpha.pop()
            if numeric:
                res = numeric.pop() + res

        return res
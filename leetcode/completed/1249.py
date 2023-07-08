class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = 0
        res = ""

        for c in s:
            if c == '(':
                left += 1
                res += c
            elif c == ')':
                if left > 0:
                    left -= 1
                    res += c
            else:
                res += c

        if left:
            temp = res
            res = ""
            for i in range(len(temp)-1, -1, -1):
                if temp[i] == '(' and left != 0:
                    left -= 1
                else:
                    res = temp[i] + res

        return res

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        lis = list(s)
        left = []

        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == ')':
                if left:
                    left.pop()
                else:
                    lis[i] = ''
        
        while left:
            lis[left.pop()] = ''

        return "".join(lis)
                
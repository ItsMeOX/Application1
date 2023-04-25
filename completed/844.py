t = '######'
s = '###'

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for letter in s:
            if letter == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(letter)
        
        stack2 = []
        for letter in t:
            if letter == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(letter)

        return stack1 == stack2           

        
        


sol = Solution()
print(sol.backspaceCompare(s,t))
    

    
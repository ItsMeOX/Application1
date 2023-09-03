
# Initialize a stack and iterate through s.
# If s == 'a': append 1 to stk
# If s == 'b': last elm of stk must be 1. Add last elm of stk by 1.
# If s == 'c': last elm of stk must be 2. If true then pop.
# For the case like 'aaabc', we have to make sure the at last the stack does not contain any element.

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for c in s:
            if c == 'a':
                stk.append(1)
            elif c == 'b':
                if not stk or stk[-1] != 1:
                    return False
                stk[-1] += 1
            else:
                if not stk or stk[-1] != 2:
                    return False
                stk.pop()
        
        return not stk
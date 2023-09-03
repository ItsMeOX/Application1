# If s[i] == '(':
# 1. left += 1, i += 1.

# If s[i] == ')':
# 1. if left == 0, 
#    res += 1
#    1. if s[i+1] != ')': res += 2, i += 1
#    2. if s[i+1] == ')': res += 1, i += 2
# 2. if left != 0,
#    left -= 1
#    1. if s[i+1] != ')': res += 1, i += 1
#    2. if s[i+1] == ')': res += 0, i += 2


class Solution:
    def minInsertions(self, s: str) -> int:
        left = 0
        res = 0

        i = 0
        while i < len(s):
            c = s[i]
            if c == '(':
                left += 1
                i += 1
            else:
                if not left:
                    if i == len(s)-1 or s[i+1] != ')':
                        res += 2
                        i += 1
                    else:
                        res += 1
                        i += 2
                else:
                    if i == len(s)-1 or s[i+1] != ')':
                        res += 1
                        i += 1
                    else:
                        i += 2    
                    left -= 1
        
        res += 2 * left
    
        return res
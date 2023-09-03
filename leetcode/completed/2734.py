
# While s[i] == 'a', keep increasing i and append s[i] to res.
# if i == len(s), as we are required to convert once, we will convert the last 'a' to 'z'.
# if s[i] != 'a', we will start converting the string from i.
# In the process of converting, if we encounter 'a', then stop converting and append the rest of s to res.
# Else, keep shifting the alphabet to left once. ('b' to 'a', 'c' to 'b')

class Solution:
    def smallestString(self, s: str) -> str:
        res = ''
        converting = False
        alpha = 'abcdefghijklmnopqrstuvwxyz'

        for i in range(len(s)):
            c = s[i]
            if not converting:
                if c == 'a':
                    res += 'a'
                else:
                    converting = True
                    res += alpha[alpha.index(c)-1]
            else:
                if c == 'a':
                    return res + s[i:]
                res += alpha[alpha.index(c)-1]

        return res if converting else res[:-1]+'z'
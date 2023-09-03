
# Initialize score with number of 1 in s.
# For every i from 0 to len(s)-2, we split the string to s[:i+1], s[i+1:].
# If the number we split is 
# 0, then score + 1,
# 1, then score - 1.
# Compare res with current score every iteration. 

class Solution:
    def maxScore(self, s: str) -> int:
        score = s.count('1')
        res = 0
        for i in range(len(s)-1):
            c = s[i]
            if c == '0':
                score += 1
            else:
                score -= 1
            res = max(res, score)

        return res
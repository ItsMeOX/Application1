
# Keep track of amount of each unique character left side of i and right side i.
# If left and right both have a character and [left, middle, right] not been seen before, then add 1 to 'res' and add [middle, left] to 'res'.
# Here left and right are same character and middle is character s[i].

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        right = {}
        left = set()
        seen = set()
        res = 0

        for c in s:
            right[c] = right.get(c, 0) + 1

        for i in range(len(s)-1):
            right[s[i]] -= 1
            if not right[s[i]]:
                del right[s[i]]
            for key in left:
                if key in right and (s[i], key) not in seen:
                    seen.add((s[i], key))
                    res += 1
            left.add(s[i])
        
        return res
    
# Keep track of first and last indices of each unique character in s.
# Then find the amount of unique characters between (left, right) and add it to 'res'.

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        indices = {}
        res = 0

        for i in range(len(s)):
            if s[i] not in indices:
                indices[s[i]] = [i, i]
            else:
                indices[s[i]][1] = i

        for l, r in indices.values():
            res += len(set(s[l+1:r]))

        return res
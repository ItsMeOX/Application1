# O(n^2) not O(n)
# Initialize two pointers left, right,
# marker which marks the index of last character of repetitive substring.
# If we first meet a repetitive substring, ignore it,
# the second time we see it, we move left and right pointers back to marker,
# and start from increasing window size from index marker.
# This is similar to string matching.

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        marker = -1
        left = right = 0
        res = 1

        while right < len(s):
            if s[right] == s[right-1]:
                if marker != -1:
                    left = marker
                    right = marker
                    marker = -1
                else:
                    marker = right
            res = max(res, right - left + 1)
            right += 1

        return res
    
# "24489929009", res = 7

# O(n) solution

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        marker = -1
        left = right = 0
        res = 1

        for right in range(len(s)):
            if s[right] == s[right-1]:
                if marker != -1:
                    left = marker
                marker = right
            res = max(res, right - left + 1)

        return res
class Solution:
    def longestPalindrome(self, s: str) -> int:
        val = dict()
        ans = 0
        for cha in s:
            if cha in val:
                val[cha] += 1
            else:
                val[cha] = 1

        for x in val.values():
            if x % 2 * 2 == 0:
                ans += x
            else:
                ans += x - 1
        
        if ans < len(s):
            return ans + 1
        else:
            return ans
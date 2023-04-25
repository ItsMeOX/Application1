class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left , right = 0 , 1
        temp_k = k
        res = 0
        while right < len(s):
            if s[left] == s[right]:
                right += 1
            elif temp_k > 0:
                right += 1
                temp_k -= 1
            else:
                res = max(res, right - left)
                left += 1
                right = left + 1
                temp_k = k

        res = max(res, right - left)
        return res


s = 'ABBB'
sol = Solution()
print(sol.characterReplacement(s,2))
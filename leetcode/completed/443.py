from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        left, right = 0, 0
        cnt = 0

        while right < len(chars):
            if chars[left] == chars[right]:
                cnt += 1
            else:
                if cnt > 1:
                    temp = str(cnt)
                    chars[left+1: left+cnt] = list(temp)
                    left += 1+len(temp)
                    right = left
                else:
                    left += 1
                cnt = 1

            right += 1

        if cnt > 1:
            temp = str(cnt)
            chars[left+1: left+cnt] = list(temp)

        return len(chars)

sol = Solution()
print(sol.compress(["a","a","b","b","c","c","c"]))
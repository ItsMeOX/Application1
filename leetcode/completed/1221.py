class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left, right = 0, 0
        res = 0

        for c in s:
            if c == 'L':
                left += 1
            else:
                right += 1

            if left == right:
                res += 1
                left = right = 0
            
        return res
    
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        res = 0

        for c in s:
            if c == 'L':
                cnt += 1
            else:
                cnt -= 1

            if not cnt:
                res += 1
            
        return res
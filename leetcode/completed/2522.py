
# For every index i, 
# we will check if s[start of last subarray ~ i] is > k or not.
# If true, then we will make a subarray s[start of last subarray ~ i - 1], and current subarray = s[i].
# s = "165462", k = 60,
# i = 0, 1 | 65462, 1 < k so continue
# i = 1, 16 | 5462, 16 < k so continue
# i = 2, 165 | 462, 165 > k so split array: 16 | 5 | 462
# i = 3, 16 | 54 | 62
# i = 4, 16 | 546 | 2, so 16 | 54 | 6 | 2
# i = 5, 16 | 54 | 62.

# After every split, we will check if the current subarray is still > k.
# If true, return -1.
# s = "238182", k = 5,
# i = 0, 2 | 38182
# i = 1, 23 | 8182, so 2 | 3 | 8182
# i = 2, 2 | 38 | 182, so 2 | 3 | 8 | 182
# but 8 > k, so return -1.

class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        cur = 0
        res = 1

        for digit in s:

            cur = cur * 10 + int(digit)

            if cur > k:
                temp = cur % 10
                res += 1
                cur = temp
        
            if cur > k: return -1

        return res


# Just simply brute force solution.

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        original = [i for i in range(n)]
        perm = [i for i in range(n)]
        temp = [0] * n
        res = 0
        while temp != original:
            for i in range(len(temp)):
                if i & 1: temp[i] = perm[n//2 + i//2]
                else: temp[i] = perm[i // 2]
            perm = list(temp)
            res += 1

        return res
    
# We can also track a index, when it is back to the same index, return res.
# (need proof)
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        i, res = 1, 0
        while res == 0 or i > 1:
            if i & 1: i = n // 2 + i // 2
            else: i = i // 2
            res += 1
        
        return res

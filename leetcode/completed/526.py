# Generate all the permutations of numbers between 1 to n.
# At index i, if temp[i] is not divisible by i or i is not divisible by temp[i], we skip it.
# We create a 'seen' set to keep track of number that is currently used in temp.
# If i successfully reach n, that means we have found a valid permutation, so add 1 to res.
# (we can also use visited array of length n instead of seen set)

class Solution:
    def countArrangement(self, n: int) -> int:
        temp = [0] * n
        res = 0
        seen = set()

        def dfs(i):
            nonlocal res
            if i == n:
                res += 1

            for k in range(1, n+1):
                if k not in seen and (k % (i+1) == 0 or (i+1) % k == 0):
                    temp[i] = k
                    seen.add(k)
                    dfs(i+1)
                    seen.remove(k)

        dfs(0)

        return res
    
class Solution:
    def countArrangement(self, n: int) -> int:
        occupied = [False] * (n+1)
        res = 0

        def dfs(i):
            nonlocal res
            if i == n:
                res += 1

            for k in range(1, n+1):
                if not occupied[k] and (k % (i+1) == 0 or (i+1) % k == 0):
                    occupied[k] = True
                    dfs(i+1)
                    occupied[k] = False

        dfs(0)

        return res
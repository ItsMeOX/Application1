
# Get the steps for each number from lo to hi (inclusive),
# then sort the array and get the kth element.

from functools import lru_cache
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        arr = []

        @lru_cache(None)
        def dfs(i):
            if i == 1: return 0
            if i &  1: return 1 + dfs(i*3+1)
            else     : return 1 + dfs(i // 2)

        for i in range(lo, hi+1):
            arr.append((dfs(i), i))

        arr.sort()

        return arr[k-1][1]
    

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def dfs(i):
            res = 0
            while i > 1:
                if i in arr:
                    return res + arr[i]
                res += 1
                if i &  1: i = i*3 + 1
                else     : i = i // 2
            return res

        arr = {}
        for i in range(lo, hi+1):
            arr[i] = dfs(i)

        keys = sorted(arr.keys(), key = lambda e: arr[e])

        return keys[k-1]
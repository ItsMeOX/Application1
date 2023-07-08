class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def check(x):
            cnt = {}
            for d in str(x):
                cnt[d] = cnt.get(d, 0) + 1
            return all(int(d) == cnt[d] for d in cnt.keys())

        while True:
            n += 1
            if check(n): return n

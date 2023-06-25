from typing import List
from bisect import bisect_left, bisect_right
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ranges = [(0,0), (s.find('|'),0)]

        first_index = s.find('|')
        for i in range(s.find('|')+1, len(s)):
            if s[i] == '|':
                ranges.append((i, ranges[-1][1]+i-first_index-1))
                first_index = i

        print(ranges)

        res = []
        for query in queries:
            # after : <= query[1]
            # first : >= query[0]
            first = bisect_right(ranges,(query[0],))
            first = first if first < len(ranges) else first - 1
            after = bisect_right(ranges,(query[1],))
            after = after if after < len(ranges) and query[1] == ranges[after][0] else after - 1
            res.append(max(0, ranges[after][1] - ranges[first][1]))

        return res

sol = Solution()

s = "*|*|||"
queries = [[0,0],[1,3]]

print(sol.platesBetweenCandles(s, queries))
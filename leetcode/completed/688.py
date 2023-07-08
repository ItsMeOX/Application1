from functools import cache
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(-1, -2),(-2, -1),(-2, 1),(-1, 2),(1, 2),(2, 1),(2, -1),(1, -2)]
        # directions = (drow, dcol)

        @cache
        def move(r, c, k):
            if k == 0:
                return 1
            k -= 1

            prob = 1
            cnt = 0

            for dr, dc in directions:
                if 0 <= r+dr < n and 0 <= c+dc < n:
                    cnt += move(r+dr, c+dc, k)
            print(cnt)
            prob *= (cnt / 8)
            return prob

        return move(row, column, k)

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float: #TIME: O(n^2 * k) SPACE: O(n^2 * k)
        directions = [(-1, -2),(-2, -1),(-2, 1),(-1, 2),(1, 2),(2, 1),(2, -1),(1, -2)]
        cnt = [[[0]*n for _ in range(n)] for _ in range(k+1)]
        cnt[0][row][column] = 1

        for _k in range(1, k+1):
            for r in range(n):
                for c in range(n):
                    if cnt[_k-1][r][c]:
                        for dr, dc in directions:
                            if 0 <= r+dr < n and 0 <= c+dc < n:
                                cnt[_k][r+dr][c+dc] += cnt[_k-1][r][c]

        _sum = 0
        for row in cnt[-1]:
            for col in row:
                _sum += col

        return _sum / (8**k) # total walkable step / total steps 

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float: #TIME: O(n^2 * k) SPACE: O(n^2)
        directions = [(-1, -2),(-2, -1),(-2, 1),(-1, 2),(1, 2),(2, 1),(2, -1),(1, -2)]
        cnt_back = [[0]*n for _ in range(n)]
        cnt_front = [[0]*n for _ in range(n)]
        cnt_back[row][column] = 1

        for _ in range(k):
            for r in range(n):
                for c in range(n):
                    if cnt_back[r][c]:
                        for dr, dc in directions:
                            if 0 <= r+dr < n and 0 <= c+dc < n:
                                cnt_front[r+dr][c+dc] += cnt_back[r][c]
            cnt_back = [[ro for ro in co] for co in cnt_front]
            cnt_front = [[0]*n for _ in range(n)]

        _sum = 0
        for row in cnt_back:
            for col in row:
                _sum += col

        return _sum / (8**k)

sol = Solution()
print(sol.knightProbability(n = 3, k = 2, row = 0, column = 0))
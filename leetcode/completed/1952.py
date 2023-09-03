class Solution:
    def isThree(self, n: int) -> bool:
        cnt = 1
        for i in range(1, n//2 + 1):
            if n % i == 0:
                cnt += 1
            if cnt > 3: break

        return cnt == 3
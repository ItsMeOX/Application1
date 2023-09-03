class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        counter = {}

        for i in range(lowLimit, highLimit+1):
            t = 0
            while i:
                t += i % 10
                i //= 10
            counter[t] = counter.get(t, 0) + 1

        return max(counter.values())
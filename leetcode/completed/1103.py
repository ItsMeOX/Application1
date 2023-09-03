from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        last = 1
        res = [0] * num_people
        while candies > 0:
            for i in range(num_people):
                if candies <= last:
                    res[i] += candies
                    candies = 0
                    break
                else:
                    res[i] += last
                    candies -= last
                    last += 1

        return res
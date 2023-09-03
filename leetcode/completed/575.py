from typing import List

# If amount of unique candies > len / 2, then return len / 2,
# else, return amount of unique candies.

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))
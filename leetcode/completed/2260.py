from typing import List

# Keep track of seen card in dictionary.
# Next time we see it, the distance will be current_i - last_seen_i + 1
# We will compare current 'res' with our distance and update 'res' if the current distance is shorter than 'res'.

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        memo = {}
        res = float('inf')

        for i in range(len(cards)):
            if cards[i] in memo:
                res = min(res, i - memo[cards[i]] + 1)
            memo[cards[i]] = i

        return res if res < float('inf') else -1
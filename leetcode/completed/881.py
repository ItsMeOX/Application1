from typing import List

# Using greedy + two pointers here.
# Sort the people from low to high first.
# If left + right does not exceed limit, add them both to boat, so left + 1 and right - 1.
# Else if exceeds limit, takes only the right people, so right - 1.
# We need to take into account of people when left == right so set the termination condition to left <= right.

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left = 0
        right = len(people) - 1
        res = 0

        people.sort()

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            res += 1
            right -= 1

        return res
from typing import List

# Initiliaze a stack.
# For each asteroid, if the asteroid is moving right, then it will not collide with previous asteroids, so just append it to stk.
# If the asteroid is moving left, we check for the following conditions:
# 1. if last asteroid is moving right and is smaller than current asteroid, keep popping them off the stack.
# 2. if last asteroid is moving right and is same size with current asteroid, pop it off and continue without appending.
# 3. if last asteroid is moving right and is larger than current asteroid, continue without popping or appending.
# The stk at last will be our answer.

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for a in asteroids:
            if a < 0:
                while stk and 0 <= stk[-1] < abs(a):
                    stk.pop()
                if stk and stk[-1] == abs(a):
                    stk.pop()
                    continue
                if stk and stk[-1] > abs(a):
                    continue
            stk.append(a)

        return stk
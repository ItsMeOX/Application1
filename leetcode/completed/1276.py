from typing import List

# let jumbo burger = x, small burger = y
#     tomato slices = a, cheese slices = b

# 4x + 2y = a  => 2x + y = a/2   ----- 1
#  x + y  = b                    ----- 2

# 1 - 2 => x = a/2 - b
#          y = b - x

# if x < 0 or y < 0 or x is floating number, there is no solution.      

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        x = tomatoSlices / 2 - cheeseSlices
        y = cheeseSlices - x

        if x < 0 or int(x) != x or y < 0:
            return []
        

        return [int(x), int(y)]
        
sol = Solution()
print(sol.numOfBurgers(tomatoSlices = 2385088, cheeseSlices = 164763))
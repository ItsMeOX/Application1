from typing import List

# Take an example:
# differences = [1, -3, 4], lower = 1 , upper = 6.
# If we take number 0 and iterate through the differences array,
# the number will be => 1 , -2 , 2
# the maximum positive offset is 2 , the maximum negative offset is -2.
# That means that, anything starting number between 
# upper - positive offset and lower + negative offset will be valid.
# Here valid numbers are: (1+2) ~ (6-2) = 3 ~ 4, so res = 2.

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        hi, lo = 0, 0
        temp = 0
        for dif in differences:
            temp += dif
            hi = max(hi, temp)
            lo = min(lo, temp)
        
        return max(0, upper-hi-(lower-lo)+1) 
# -lo becuz lo is a negative number.
# upper-hi-(lower+(-lo))+1.
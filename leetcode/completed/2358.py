from typing import List

# My approach:
# Sort the grades in increasing order.
# Find an interval where 'current people number' and 'current grade' are both larger than previous ones.
# If we found one such interval, write 'current data' to 'prev data' and reset 'current data', we also add 1 to res.
# Finally return the res after iteration.

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort()
        res = 0
        cur_grade = cur_count = 0
        prev_grade = prev_count = 0
        right = 0

        for right in range(len(grades)):
            cur_grade += grades[right]
            cur_count += 1
            if cur_grade > prev_grade and cur_count > prev_count:
                prev_grade = cur_grade
                prev_count = cur_count
                cur_grade = 0
                cur_count = 0
                res += 1

        return res
    
# But, notice that we do not need to care about the number,
# For example: [1,1,1],
# the groups will be [1], [1,1],
# and grade and count of second group will always be larger than the first one.
# So, we just need to count how large of triangle we can form from length of our 'grades list'.
# It is triangle because that the size of groups will be:
# [1]
# [1,1]
# [1,1,1].

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        k = 1
        n = len(grades)

        while k * (k+1) // 2 <= n: # can also binary search instead of linear search.
            k += 1
        
        return k-1

# O(1) solution:
# class Solution:
#     def maximumGroups(self, grades: List[int]) -> int:
#         return floor((-1 + (1 + 8 * len(grades)) ** 0.5) / 2)
    
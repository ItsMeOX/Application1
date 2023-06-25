from typing import List
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        left, right = 0, len(plants)-1
        A_t, B_t = capacityA, capacityB
        res = 0

        while (left <= right):
            if left == right:
                if capacityA - plants[left] < 0 and capacityB - plants[left] < 0:
                    res += 1
            else:

                if capacityA - plants[left] < 0:
                    res += 1
                    capacityA = A_t
                capacityA -= plants[left]
                
                if capacityB - plants[right] < 0:
                    res += 1
                    capacityB = B_t
                capacityB -= plants[right]


            left += 1
            right -= 1

        return res

sol = Solution()
print(sol.minimumRefill( plants = [1,2,4,4,5], capacityA = 6, capacityB = 5))
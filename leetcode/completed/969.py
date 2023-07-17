from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []

        for right in range(len(arr), 0, -1):
            max_idx = 0
            for i in range(right):
                if arr[i] > arr[max_idx]:
                    max_idx = i

            if max_idx < right - 1:
                arr[:max_idx+1] = reversed(arr[:max_idx+1])
                arr[:right] = reversed(arr[:right])
                res.append(max_idx+1)
                res.append(right)

        return res



# 3 2 4 1 -> 2
# 4 2 3 1 -> 4
# 1 3 2 4 -> 1
# 3 1 2 4 -> 3
# 2 1 3 4 -> 1
# 1 2 3 4


# 1 4 5 2 3
# 5 4 1 2 3
# 3 2 1 4 5
# 1 2 3 4 5


# 1 3 2 5 4
# 5 2 3 1 4
# 4 1 3 2 5
# 2 3 1 4 5
# 3 2 1 4 5
# 1 2 3 4 5
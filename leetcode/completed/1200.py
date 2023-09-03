from typing import List

# Sort the array first and check if arr[i+1] - arr[i] for i is in range(1, len(arr)), is smaller then min_diff.
# If it is smaller then reset 'res' list and update 'min_diff',
# else if arr[i+1] - arr[i] == min_diff then append the pair to 'res'.

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = arr[1] - arr[0]
        res = []

        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] < min_diff:
                res = [[arr[i], arr[i+1]]]
                min_diff = arr[i+1] - arr[i]
            elif arr[i+1] - arr[i] == min_diff:
                res.append([arr[i], arr[i+1]])

        return res
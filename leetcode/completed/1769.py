from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        prefix = [0] * (n+1)
        suffix = [0] * (n+1)

        occupied = 0
        for i in range(1, n+1):
            if boxes[i-1] == '1':
                occupied += 1
            prefix[i] = prefix[i-1] + occupied

        occupied = 0
        for i in range(n-1, -1, -1):
            if boxes[i] == '1':
                occupied += 1
            suffix[i] = suffix[i+1] + occupied

        res = []
        for i in range(n):
            res.append(prefix[i] + suffix[i+1])

        return res
    
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        leftCount, leftMove = 0, 0
        rightCount, rightMove = 0, 0

        for i in range(1, n):
            if boxes[i-1] == '1':
                leftCount += 1
            leftMove += leftCount
            res[i] = leftMove

        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1':
                rightCount += 1
            rightMove += rightCount
            res[i] += rightMove

        return res
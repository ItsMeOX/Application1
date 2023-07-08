from typing import List
from heapq import heappop, heappush

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        res = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if len(heap) < k:
                    heappush(heap, (-nums1[i]-nums2[j], i, j))
                else:
                    if -nums1[i] - nums2[j] > heap[0][0]:
                        heappop(heap)
                        heappush(heap, (nums1[i]+nums2[j], i, j))
                    else:
                        break

        for _ in range(k):
            if not heap:
                break
            val, i, j = heappop(heap)
            res.append([nums1[i],nums2[j]])

        return res
    
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        l1, l2 = len(nums1), len(nums2)

        heap = [(nums1[0]+nums2[0], 0, 0)]
        visited = set((0,0))
        res = []

        while k > 0 and heap:
            _, i, j = heappop(heap)
            res.append((nums1[i], nums2[j]))
            k -= 1

            if i+1 < l1 and (i+1, j) not in visited:
                heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
                visited.add((i+1, j))
            if j+1 < l2 and (i, j+1) not in visited:
                heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
                visited.add((i, j+1))

        return res
sol = Solution()
print(sol.kSmallestPairs([1,1,2], [1,2,3], 2))
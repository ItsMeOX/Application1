class Solution:
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # """
        # Do not return anything, modify nums1 in-place instead.
        # """
        # O(nlogn) for .sort()
        # p = -1
        # for _ in range(len(nums2)):
        #     nums1[p] = nums2[p]
        #     p -= 1
        
        #nums1.sort()
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m + n - 1
        p2 = n - 1
        pl = m - 1

        while p2 > -1:
            if pl > -1 and nums1[pl] > nums2[p2]:
                nums1[p1] = nums1[pl]
                pl -= 1
            else:
                nums1[p1] = nums2[p2]
                p2 -= 1
            p1 -= 1


sol = Solution()
print(sol.merge(nums1 = [2,0], m = 1, nums2 = [1], n = 1))

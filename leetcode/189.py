# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         l = len(nums)
#         if k > l:
#             k %= l
#         nums[:] = nums[-k:] + nums[:-k]


def rotate(nums: list[int], k: int) -> None:
	L = len(nums)
	if L == k: return

	k = k%L # the case when k > L
	nums.reverse()

	for i in range(k//2):
		nums[i], nums[k-1-i] = nums[k-1-i], nums[i]

	for i in range(k, L-k):
		nums[i], nums[L-1-i+k] = nums[L-1-i+k], nums[i]

nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums)
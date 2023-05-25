class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = 1 + dic.get(num, 0)
        print(dic)
        return max(dic, key=dic.get)
  
# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         candidate = 0
#         count = 0
#         for num in nums:
#             if count == 0:
#                 candidate = num
#             if num == candidate:
#                 count += 1
#             else:
#                 count -= 1

#         return candidate            


sol = Solution()
print(sol.majorityElement([6,5,5]))
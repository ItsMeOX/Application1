# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         left , right = 0 , len(numbers) - 1
#         while True:
#             res = numbers[left] + numbers[right]
#             if res < target:
#                 left += 1
#             elif res > target:
#                 right -= 1
#             else:
#                 return [left+1 , right+1]
                
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left , right = 0 , len(numbers) - 1
        middle = (left + right)//2
        while True:
            res = numbers[middle] + numbers[middle+1]
            if res < target:
                middle += 1
            elif res > target:
                middle -= 1
            else:
                l = len(numbers) % 2
                print(l)
                return [middle+l , middle+1+l]
                
sol = Solution()
numbers = [2,3,4]
print(sol.twoSum(numbers, 6))
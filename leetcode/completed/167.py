class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left , right = 0 , len(numbers) - 1
        while True:
            res = numbers[left] + numbers[right]
            if res < target:
                left += 1
            elif res > target:
                right -= 1
            else:
                return [left+1 , right+1]

sol = Solution()
numbers = [2,3,4]
print(sol.twoSum(numbers, 6))


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        middle = 0
        
        while(low <= high):
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
            
            print(middle)
        return -1    

sol = Solution()

print(sol.search([-1,0,3,5,9,12],9))
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left , right = 0 , len(height) - 1
        MaxArea = 0
        while left < right:
            MaxArea = max(MaxArea, min(height[left], height[right]) * (right-left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            


        return MaxArea
    
# while height < min_height of left & right , can keep inc / dec left / right

sol = Solution()
height = [1,8,6,2,5,4,8,3,7] #155



print(sol.maxArea(height))
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        unique = dict() #(val, idx)
        l = 0
        s = 0
        res = 0

        for r in range(len(nums)):
            if r - l == k:
                res = max(res, s)
                s -= nums[l]
                del unique[nums[l]]
                l += 1

            if nums[r] in unique:
                l = unique[nums[r]] + 1
                toBeRemoved = []
                for key in unique.keys():
                    if unique[key] < l:
                        s -= key
                        toBeRemoved.append(key)
                for i in toBeRemoved:
                    del unique[i]
                unique[nums[r]] = r
            
            s += nums[r]
            unique[nums[r]] = r
        
        if sum(nums[-k:]) == s:
            return max(s, res)
        return res

sol = Solution()
print(sol.maximumSubarraySum(nums = [3,2,3,1], k = 3))
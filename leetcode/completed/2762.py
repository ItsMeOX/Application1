from typing import List

# Tips: if we want to count number of subarrays, the count will be: (right - left + 1) for every right from 0 to n.
# Here we iterate i from 0 to len of nums, and we keep track of the numbers in current subarray in dictionary 'counter'.
# Here because the most amount of keys in counter will be at most 5, so min and max here are O(1) operations.
# Then we get max val and min val from counter, subtract them,
# if the difference is > 2, then subtract the amount of number of nums[left] from counter and increase left by 1,
# if nums[left] in counter == 0 then delete it from counter,
# we keep doing this until max - min in counter is <= 2.
# Then count the number of subarrays which is right - left + 1 and add it to 'res'.

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        counter = {}
        left = 0
        res = 0

        for i in range(len(nums)):
            num = nums[i]
            counter[num] = counter.get(num, 0) + 1
        
            while max(counter) - min(counter) > 2:
                counter[nums[left]] -= 1

                if counter[nums[left]] == 0:
                    del counter[nums[left]]
            
                left += 1

            res += i - left + 1
        
        return res
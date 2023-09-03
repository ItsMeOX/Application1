from typing import List

# Iterate i from 0 to last elm of nums,
# iterate j from i to last elm of nums,
# if nums[j] % p == 0,
# then cnt += 1,
# if cnt > k, then break the loop as the amount of elm that is divisible by p > k,
# else append the tupled subarray (to enable hashing) to 'res',
# at last the amount of unique subarrays in 'res' will be the res.

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        res = set()

        for i in range(len(nums)):
            temp = []
            cnt = 0
            for j in range(i, len(nums)):
                if nums[j] % p == 0:
                    cnt += 1
                if cnt > k:
                    break
                temp.append(nums[j])

                if (x:=tuple(temp)) not in res:
                    res.add(x)
        
        return len(res)
    
# Optimization:
# Instead of storing the entire tupled subarray into 'res',
# we can utilize trie here and we keep track of sequence of each subarray,
# if we can form a new subtree in trie, then add 1 to res,
# traverse to respective subtree after every iteration of j.

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        res = 0
        trie = {}

        for i in range(len(nums)):
            cur = trie
            cnt = 0
            for j in range(i, len(nums)):
                if nums[j] % p == 0:
                    cnt += 1
                
                if cnt > k:
                    break
                
                if nums[j] not in cur:
                    cur[nums[j]] = {}
                    res += 1
                cur = cur[nums[j]]

        return res
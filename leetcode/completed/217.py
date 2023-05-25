class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        repeated = set()
        for num in nums:
            if num in repeated:
                return True

            repeated.add(num)

        return False
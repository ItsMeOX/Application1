from typing import List

# Consider randomly picked derived: [1 1 0 1 0 1 1]
# Starting from n = 0, we set the 'original' array to start with 0.
# derived: 1 1 0 1 0 1 1
#          0                  -> set the first element to be either 1 or 0, I picked 0 here.
#          0 1                -> for n = 0, because it is 1, so the second element in 'original' has to be 1.
#          0 1 0              -> for n = 1, it is 1, so the next element has to be flipped.
#          0 1 0 0            -> for n = 2, it is 0, so the next element has to be the same.
#          0 1 0 0 1          -> for n = 3, it is 1, so the next element has to be flipped.
#          0 1 0 0 1 1
#          0 1 0 0 1 1 0
# At last index of 'derived' array, we check:
# 1. if last element of 'derived' is 0, that means that the first and last element of 'original' has to be different.
# 2. if last element of 'derived' is 1, that means that the first and last element of 'original' has to be the same .
# In this case, the last element of 'derived' is 1, and the first and last element of 'original' are same, so the answer will be false.

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        head = False

        for i in range(len(derived)-1):
            if derived[i]:
                head = not head

        if derived[-1] == 1:
            return head == True
        else:
            return head == False
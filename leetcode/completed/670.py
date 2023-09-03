
# For every num[i], swap the digit with the (last and > num[i] and largest) digit after index i.

class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))

        for i in range(len(num)):
            largest_index = i
            largest_number = int(num[i]) + 1
            for j in range(i+1, len(num)):
                if int(num[j]) >= largest_number:
                    largest_index = j
                    largest_number = int(num[j])
            if largest_index != i:
                num[i], num[largest_index] = num[largest_index], num[i]
                break
        
        return int(''.join(num))
    

# Optimization: O(N),
# instead of looping every digit after index i,
# we can just keep track of last occurence index of every digit.

class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        last = {int(digit): i for i, digit in enumerate(num)}

        for i in range(len(num)):

            for j in range(9, int(num[i]), -1):

                if j in last and last[j] > i:

                    num[last[j]], num[i] = num[i], num[last[j]]

                    return int(''.join(num))

        return int(''.join(num))
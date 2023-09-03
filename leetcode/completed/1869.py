class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zeros = ones = 0
        longest_zeros = longest_ones = 0

        for c in s:
            if c == '0':
                zeros += 1
                ones = 0
                longest_zeros = max(longest_zeros, zeros)
            else:
                ones += 1
                zeros = 0
                longest_ones = max(longest_ones, ones)
        
        return longest_ones > longest_zeros
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix = [0] * len(customers)
        suffix = [0] * len(customers)
        if customers[-1] == 'Y':
            suffix[-1] = 1
        if customers[0] == 'N':
            prefix[0] = 1


        for i in range(1, len(customers)):
            if customers[i] == 'N':
                prefix[i] += 1
            prefix[i] += prefix[i-1]

        for i in range(len(customers)-2, -1, -1):   
            if customers[i] == 'Y':
                suffix[i] += 1
            suffix[i] += suffix[i+1]

        res = 0
        max_sum = float('inf')
        for i in range(len(customers)):
            if prefix[i] + suffix[i] < max_sum:
                res = i
                max_sum = prefix[i] + suffix[i]

        return res + 1 if res or customers[0] == 'Y' else 0

#   Y Y N Y
# c 3 2 1 1
# o 0 0 1 1

#   Y Y N Y N Y
# c 4 3 2 2 1 1
# o 0 0 1 1 2 2

# Y Y N Y N Y Y Y Y Y Y
# c 9 8 7 6 6 5 4 3 2 1
# o 0 1 1 2 2 2 2 2 2 2

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = min_penalty = customers.count('Y')
        res = 0

        for i, c in enumerate(customers):
            if c == 'Y':
                penalty -= 1
            else:
                penalty += 1
            
            if penalty < min_penalty:
                min_penalty = penalty
                res = i + 1
        
        return res


#   Y Y N Y
# c 3 2 1 1
# o 0 0 1 1

#   Y Y N Y N Y
# c 4 3 2 2 1 1
# o 0 0 1 1 2 2

# Y Y N Y N Y Y Y Y Y Y
# c 9 8 7 6 6 5 4 3 2 1
# o 0 1 1 2 2 2 2 2 2 2
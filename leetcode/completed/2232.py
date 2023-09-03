
# Iterate i from 0 to len(one)-1.
# Iterate j from 1 to len(two).
# Here i and j are the index where we put the parenthesis,
# we split one/two to front and back at the position of the parenthesis,
# then res = front_one * (back_one + front_two) * back_two. 
# If front_one is empty / back_two is empty, then we must multiply 1, so set it them to 1 if they are null.

class Solution:
    def minimizeResult(self, expression: str) -> str:
        one, two = expression.split('+')
        best_i, best_j = 0, 0
        best = float('inf')

        for i in range(len(one)-1, -1, -1):
            front_one = int(one[:i]) if one[:i] else 1
            back_one = int(one[i:])
            for j in range(1, len(two)+1):
                front_two = int(two[:j])
                back_two = int(two[j:]) if two[j:] else 1
                if front_one * (back_one + front_two) * back_two < best:
                    best = front_one * (back_one + front_two) * back_two
                    best_i, best_j = i, j
    
        return one[:best_i] + '(' + one[best_i:] + '+' + two[:best_j] + ')' + two[best_j:]
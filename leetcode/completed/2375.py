class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = [1]

        cur_d = 0
        for p in pattern:
            if p == 'D':
                cur_d += 1
                stack[-1] += 1
            else:
                temp = stack[-1]
                while cur_d:
                    stack.append(stack[-1] - 1)
                    cur_d -= 1
                stack.append(temp + 1)

        while cur_d:
            stack.append(stack[-1] - 1)
            cur_d -= 1


        return "".join([str(i) for i in stack])
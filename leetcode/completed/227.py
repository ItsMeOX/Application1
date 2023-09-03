class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        s += '#'
        num_stk = []
        cur_opr = '+'
        temp = 0

        for c in s:
            if c.isnumeric():
                temp = temp * 10 + int(c)
            else:
                if cur_opr == '+':
                    num_stk.append(temp)
                elif cur_opr == '-':
                    num_stk.append(-temp)
                elif cur_opr == '*':
                    num_stk[-1] *= temp
                else:
                    if num_stk[-1] < 0:
                        num_stk[-1] = - ( -num_stk[-1] // temp )
                    else:
                        num_stk[-1] //= temp
                cur_opr = c
                temp = 0
        
        return sum(num_stk)
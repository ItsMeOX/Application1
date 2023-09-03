
# Replace - with +- as we will split the equation by the character '+'.
# Get left and right hand side x and val, then evaluate left - right val / left - right x.

class Solution:
    def solveEquation(self, equation: str) -> str:
        equation = equation.replace('-', '+-')            

        eq_index = equation.index('=')

        lhs_x = lhs_val = 0
        rhs_x = rhs_val = 0

        for num in equation[:eq_index].split('+'):
            if not num: continue
            if num[-1] == 'x':
                if len(num) > 1:
                    lhs_x += -1 if num[-2] == '-' else int(num[:-1])
                else:
                    lhs_x += 1
            else:
                lhs_val += int(num)
        
        for num in equation[eq_index+1:].split('+'):
            if not num: continue
            if num[-1] == 'x':
                if len(num) > 1:
                    rhs_x += -1 if num[-2] == '-' else int(num[:-1])
                else:
                    rhs_x += 1
            else:
                rhs_val += int(num)

        dx = lhs_x - rhs_x
        dval = lhs_val - rhs_val

        if dx == 0 and dval == 0: return "Infinite solutions"
        elif dx == 0 and dval != 0: return "No solution"
        else: return f"x={dval // -dx}"
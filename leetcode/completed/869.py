class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_counter = {}
        for d in str(n):
            n_counter[d] = n_counter.get(d, 0) + 1
        
        for i in range(30):
            counter = {}
            cur_pow_num = str(1 << i)
            for d in cur_pow_num:
                counter[d] = counter.get(d, 0) + 1

            if counter == n_counter:
                return True

        return False
    
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_list = sorted(str(n))

        i = 0
        while len(str(1 << i)) <= len(n_list):
            if sorted(str(1 << i)) == n_list:
                return True
            i += 1

        return False
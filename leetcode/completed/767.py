from heapq import heappop, heappush, heapify

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        
        heap = [(-counter[key], key) for key in counter.keys()]
        heapify(heap)

        res = ''
        while heap:
            first_cnt, first_chr = heappop(heap)
            if not res or res[-1] != first_chr:
                res += first_chr
                if first_cnt + 1 != 0:
                    heappush(heap, (first_cnt + 1, first_chr))
            else:
                if not heap: return ''
                second_cnt, second_chr = heappop(heap)
                res += second_chr
                if second_cnt + 1 != 0:
                    heappush(heap, (second_cnt + 1, second_chr))
                heappush(heap, (first_cnt, first_chr))

        return res
    
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        
        heap = [(-counter[key], key) for key in counter.keys()]
        heapify(heap)

        res = ''
        while len(heap) > 1:
            first_cnt, first_chr = heappop(heap)
            second_cnt, second_chr = heappop(heap)
            res += first_chr
            res += second_chr
            if first_cnt + 1 != 0:
                heappush(heap, (first_cnt + 1, first_chr))
            if second_cnt + 1 != 0:
                heappush(heap, (second_cnt + 1, second_chr))

        if heap:
            if heap[0][0] == -1:
                res += heap[0][1]
            else:
                res = ''

        return res
    
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = {}
        max_key = ''
        max_freq = 0
        n = len(s)

        for c in s:
            counter[c] = counter.get(c, 0) + 1
            if counter[c] > max_freq:
                max_freq = counter[c]
                max_key = c

        if max_freq > (len(s)+1) // 2:
            return ''

        res = ['']*n
        i = 0

        for _ in range(counter[max_key]):

            res[i] = max_key
            i += 2

        del counter[max_key]

        for key in counter:
            for _ in range(counter[key]):
                
                if i >= n: i = 1

                res[i] = key
                i += 2

        return ''.join(res)
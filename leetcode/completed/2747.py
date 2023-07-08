from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        queries = sorted([[queries[i], i] for i in range(len(queries))])
        logs.sort(key = lambda e: e[1])

        server_cnt = {i: 0 for i in range(1, n+1)} 
        cur_cnt = 0
        left, right = 0, 0

        res = [0] * len(queries)

        # logs => [serv_id, time]
        # queries => [idx, time]

        for q, i in queries:
            while right < len(logs) and logs[right][1] <= q:
                serv_id = logs[right][0]
                if server_cnt[serv_id] == 0:
                    cur_cnt += 1
                server_cnt[serv_id] += 1
                right += 1

            while left < len(logs) and logs[left][1] < q-x:
                serv_id = logs[left][0]
                server_cnt[serv_id] -= 1
                if server_cnt[serv_id] == 0:
                    cur_cnt -= 1
                left += 1

            res[i] = n - cur_cnt

        return res
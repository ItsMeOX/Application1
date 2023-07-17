from typing import List

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 <= runningCost: return -1
        
        profit = [0, 0]
        boarded_cus = 0
        waiting_cus = 0
        turn = 0

        for customer in customers:
            waiting_cus += customer
            turn += 1
            if waiting_cus >= 4:
                waiting_cus -= 4
                boarded_cus += 4
            else:
                boarded_cus += waiting_cus
                waiting_cus = 0
            cur_profit = boarded_cus * boardingCost - turn * runningCost
            if profit[0] < cur_profit:
                profit[0] = cur_profit
                profit[1] = turn

        while waiting_cus:
            turn += 1

            if waiting_cus >= 4:
                waiting_cus -= 4
                boarded_cus += 4
            else:
                boarded_cus += waiting_cus
                waiting_cus = 0

            # to_be_boarded = min(4, waiting_cus)
            # waiting_cus -= to_be_boarded
            # boarded_cus += to_be_boarded

            cur_profit = boarded_cus * boardingCost - turn * runningCost
            if profit[0] < cur_profit:
                profit[0] = cur_profit
                profit[1] = turn

        return profit[1] if profit[1] else -1
from typing import List
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        sum_ = sum(prices[:2])
        return money - sum_ if sum_ <= money else money
    
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_price, sec_min_price = 100, 100

        for price in prices:
            if price < min_price:
                sec_min_price = min_price
                min_price = price
            elif price < sec_min_price:
                sec_min_price = price
        
        return money - min_price - sec_min_price if min_price + sec_min_price <= money else money
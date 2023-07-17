from typing import List

class ATM:

    def __init__(self):
        self.storage = [0] * 5 # 20, 50, 100, 200, 500
        self.mapper = {0: 20, 1: 50, 2: 100, 3: 200, 4: 500}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.storage[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        temp = list(self.storage)
        res = [0] * 5

        for i in range(4, -1, -1):
            note_needed = amount // self.mapper[i]
            min_amount = min(temp[i], note_needed)
            amount -= min_amount * self.mapper[i]
            res[i] += min_amount
            temp[i] -= min_amount

        if amount:
            return [-1]
        
        self.storage = temp

        return res



# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
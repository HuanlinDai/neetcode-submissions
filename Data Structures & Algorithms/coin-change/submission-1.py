class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amts = {0:0}
        for total in range(1,amount+1):
            for coin in coins:
                if total - coin in amts:
                    amts[total] = min(amts[total-coin] + 1, amts.get(total,amount+1))

        return amts.get(amount, -1)
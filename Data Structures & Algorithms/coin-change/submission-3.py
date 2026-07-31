class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amts = {0:0}
        for amt in range(1,amount+1):
            for coin in coins:
                if amt - coin in amts:
                    amts[amt] = min(amts.get(amt, float('inf')), amts[amt-coin] + 1)
        
        return amts.get(amount, -1)
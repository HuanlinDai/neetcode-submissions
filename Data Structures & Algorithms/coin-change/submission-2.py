class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        amts = {0:0}

        for total in range(amount+1):
            for coin in coins:
                if total-coin in amts:
                    amts[total] = min(amts.get(total,float('inf')), 1 + amts[total-coin])
        
        return amts.get(total,-1)
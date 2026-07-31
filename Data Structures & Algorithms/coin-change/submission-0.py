class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        possible = {0:0}
        for total in range(amount+1):
            for coin in coins:
                if total - coin in possible:
                    possible[total] = min(possible.get(total,float('inf')), possible[total-coin] + 1)
            
        if amount not in possible:
            return -1
        return possible[amount]
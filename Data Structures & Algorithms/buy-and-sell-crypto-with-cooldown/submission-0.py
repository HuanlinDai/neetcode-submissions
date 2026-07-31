class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * (n+1) for _ in range(2)]
        
        for i in range(n-1, -1, -1):
            #buying
            buy = dp[False][i+1]-prices[i]
            cooldown = dp[True][i+1]
            dp[True][i] = max(buy,cooldown)
            #selling
            sell = prices[i]
            if i + 2 <= n:
                sell += dp[True][i+2]
            cooldown = dp[False][i+1]
            dp[False][i] = max(sell,cooldown)

        return dp[True][0]
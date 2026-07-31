class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp_chill = 0
        dp_hold = float('-inf')
        dp_sold = 0

        for p in prices:
            dp_chill, dp_hold, dp_sold = max(dp_chill, dp_sold), max(dp_hold, dp_chill-p), dp_hold + p
        return max(dp_chill, dp_sold)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {0:1}
        for k in nums:
            newdp = {}
            for i in dp:
                newdp[i-k] = newdp.get(i-k,0) + dp[i]
                newdp[i+k] = newdp.get(i+k,0) + dp[i]
            dp = newdp
        return dp.get(target,0)
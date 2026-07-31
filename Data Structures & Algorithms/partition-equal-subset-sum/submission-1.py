class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        total //= 2
        n = len(nums)
        dp = [False] * (total + 1)
        dp[0]= True
        for row in range(n):
            for col in range(total, nums[row]-1, -1):
                dp[col] = dp[col] or dp[col - nums[row]]
        return dp[-1]

        
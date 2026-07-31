class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        total //= 2
        n = len(nums)
        dp = [[False] * (total + 1) for _ in range(n)]
        for row in range(n):
            dp[row][total] = True

        for row in range(n-1, -1, -1):
            for col in range(total, -1, -1):
                if dp[row][col]:
                    dp[row-1][col-nums[row]] = True
                    dp[row-1][col] = True

        return dp[0][0]

        
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        
        def dfs(l,r):
            if r < 0 or l >= n or l > r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            
            left = nums[l-1] if l-1 >= 0 else 1
            right = nums[r+1] if r+1 <= n-1 else 1

            cur = 0
            for i in range(l, r+1):
                cur = max(cur, left * nums[i] * right + dfs(l, i-1) + dfs(i+1,r))
            dp[(l,r)] = cur
            return cur

        return dfs(0,n-1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxjump = 0
        n = len(nums)
        for i in range(n):
            if maxjump < i:
                return False
            elif maxjump >= n-1:
                return True
            maxjump = max(maxjump, i + nums[i])
        return True
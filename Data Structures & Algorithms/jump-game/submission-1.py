class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        best = 0
        for i in range(len(nums)):
            if best < i:
                return False
            best = max(best, i + nums[i])
        return True
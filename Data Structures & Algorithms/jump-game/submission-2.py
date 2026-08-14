class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for i in range(len(nums)-1):
            gas = max(gas, nums[i])
            if gas == 0:
                return False
            gas -= 1
        return True
            
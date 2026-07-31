class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        elif len(nums) == 3:
            return max(nums[1], nums[0] + nums[2])
        maxrob = [0] * len(nums)
        maxrob[0] = nums[0]
        maxrob[1] = nums[1]
        maxrob[2] = nums[2] + nums[0]
        for i in range(3,len(nums)):
            maxrob[i] = nums[i] + max(maxrob[i-2], maxrob[i-3])
        return max(maxrob[-2:])
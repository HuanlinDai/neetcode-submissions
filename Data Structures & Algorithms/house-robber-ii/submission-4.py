class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
        if len(nums) < 3:
            return max(nums)

        threebefore = nums[0]
        twobefore = nums[1]
        onebefore = nums[2] + threebefore
        for i in range(3,len(nums)):
            now = nums[i] + max(threebefore, twobefore)
            threebefore = twobefore
            twobefore = onebefore
            onebefore = now
        return max(onebefore, twobefore)
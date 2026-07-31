class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        if len(nums) < 3:
            return max(nums)
        threebefore = nums[0]
        twobefore = nums[1]
        onebefore = nums[2] + threebefore
        for i in range(3, len(nums)):
            now = max(twobefore, threebefore) + nums[i]
            threebefore = twobefore
            twobefore = onebefore
            onebefore = now

        return max(twobefore, onebefore)

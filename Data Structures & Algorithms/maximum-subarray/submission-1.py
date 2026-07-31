class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curmax = float('-inf')
        for num in nums:
            curmax = max(curmax + num, num)
            res = max(curmax, res)
        return res
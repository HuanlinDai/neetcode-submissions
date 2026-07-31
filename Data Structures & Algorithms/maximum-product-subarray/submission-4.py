class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]

        curmax = 1
        curmin = 1
        for i in range(len(nums)):
            tmp = nums[i] * curmax
            curmax = max(tmp, nums[i] * curmin, nums[i])
            curmin = min(tmp, nums[i] * curmin, nums[i])
            res = max(res, curmax)

        return res
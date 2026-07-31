class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = minprod = 1
        res = nums[0]
        for num in nums:
            tmp = num * maxprod
            maxprod = max(num, tmp, num * minprod)
            minprod = min(num, tmp, num * minprod)
            res = max(maxprod, res)
        return res
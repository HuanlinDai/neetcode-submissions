class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for k in nums:
            res ^= k
        return res
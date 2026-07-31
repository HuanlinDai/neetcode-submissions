class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))


    def helper(self, l):
        a, b, c = 0, 0, 0
        for k in l:
            a, b, c = b, c, max(a, b) + k
        return max(b, c)
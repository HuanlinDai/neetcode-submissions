class Solution:
    def rob(self, nums: List[int]) -> int:
        a = b = c = 0
        for i in range(len(nums)):
            a, b, c = b, c, nums[i] + max(a, b)

        return max(a,b,c)
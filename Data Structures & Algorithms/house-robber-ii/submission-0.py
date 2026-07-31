class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max([self.helper(nums[1:]), self.helper(nums[:-1])])
    def helper(self, arr):
        rob1 = 0
        rob2 = 0
        for k in arr:
            newrob = max(k + rob1, rob2)
            rob1 = rob2
            rob2 = newrob
        return rob2

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]

        nums.sort()

        n = len(nums)
        idx = 0
        prev = 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                idx = prev
            else:
                idx = 0
            prev = len(res)
            for j in range(idx, prev):
                new = res[j] + [nums[i]]
                res.append(new)

        return res
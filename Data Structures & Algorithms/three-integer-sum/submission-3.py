class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resset = set()
        n = len(nums)
        for k in range(n-1, -1, -1):
            i, j = 0, k-1
            while i < j:
                cursum = nums[i] + nums[j] + nums[k]
                if cursum == 0:
                    resset.add((nums[i], nums[j], nums[k]))
                    i += 1
                    j -= 1
                elif cursum > 0:
                    j -= 1
                else:
                    i += 1
        return list(resset)
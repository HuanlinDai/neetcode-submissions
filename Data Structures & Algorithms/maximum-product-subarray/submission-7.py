class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = cur = lowcur = nums[0]
    
        for i in range(1, len(nums)):
            tmp = nums[i] * cur
            cur = max(nums[i], tmp, lowcur * nums[i])
            lowcur = min(nums[i], nums[i] * lowcur, tmp)
            res = max(res, cur)

        return res
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:    
        k = 0
        j = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == val:
                while j >= 0 and nums[j] == val:
                    j -= 1
                if i >= j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            k += 1
        return k
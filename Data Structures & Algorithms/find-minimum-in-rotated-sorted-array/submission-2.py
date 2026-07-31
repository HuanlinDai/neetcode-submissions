class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        l = 0
        r = n - 1
        m = (l+r)//2

        while l < r:
            if nums[m] <= nums[(m+1)%n] and nums[m] <= nums[(m-1)%n]:
                return nums[m]
            
            elif not (nums[r] < nums[m] and nums[r] < nums[l]):
                r = m - 1
            else:
                l = m + 1
            m = (l+r)//2

        return nums[m]

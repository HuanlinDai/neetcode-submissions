class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        for i in range(len(nums)-1):
            prefix.append(prefix[-1] * nums[i])
            suffix.append(suffix[-1] * nums[len(nums)-i-1])
        suffix.reverse()
        return [prefix[i] * suffix[i] for i in range(len(nums))]
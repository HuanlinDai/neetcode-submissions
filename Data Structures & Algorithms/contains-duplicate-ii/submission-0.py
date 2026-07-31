class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        seen = {nums[0]}
        n = len(nums)
        for j in range(1,n):
            if j-i > k:
                seen.remove(nums[i])
                i += 1
            if nums[j] in seen:
                return True
            seen.add(nums[j])
        return False
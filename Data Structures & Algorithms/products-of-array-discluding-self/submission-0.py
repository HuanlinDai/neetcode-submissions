class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        pref[0] = suff[-1] = 1
        for i in range(1,n):
            pref[i] = pref[i-1] * nums[i-1]
            suff[n-1-i] = suff[n-i] * nums[n-i]
        res = []
        for i in range(n):
            res.append(pref[i] * suff[i])
        return res
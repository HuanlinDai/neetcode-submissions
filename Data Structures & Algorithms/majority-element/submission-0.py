class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqs = Counter(nums)
        n = len(nums)
        for i in freqs:
            if freqs[i] > n//2:
                return i
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        for start in hashset:
            if start-1 not in hashset:
                cur = 0
                while start in hashset:
                    start += 1
                    cur += 1
                res = max(res, cur)
        return res
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset = set(nums)
        res = 0
        for e in numset:
            if e - 1 not in numset:
                cur = e
                curlen = 0
                while e in numset:
                    curlen += 1
                    e += 1
                res = max(res, curlen)
        return res
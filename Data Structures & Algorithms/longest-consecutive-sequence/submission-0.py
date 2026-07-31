class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for num in hashset:
            if num-1 not in hashset:
                #start of sequence:
                cur = num
                curlen = 1
                while cur + 1 in hashset:
                    cur += 1
                    curlen += 1

                longest = max(longest, curlen)
        return longest
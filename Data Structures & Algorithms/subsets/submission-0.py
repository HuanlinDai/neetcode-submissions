class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        for k in nums:
            newset = []
            for subset in res:
                if len(subset) > 0:
                    if subset[-1] >= k:
                        continue
                newset.append(subset + [k])
            res += newset
        return res

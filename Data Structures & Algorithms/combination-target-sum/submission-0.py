class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ind = {nums[i] : i for i in range(len(nums))}
        q = [[]]
        res = []
        while q:
            l = q.pop(0)
            if len(l) == 0:
                lastind = 0
            else:
                lastind = ind[l[-1]]
            cursum = sum(l)   
            for i in range(lastind, len(nums)):
                newsum = cursum + nums[i]
                if newsum < target:
                    q.append(l + [nums[i]])
                elif newsum == target:
                    res.append(l + [nums[i]])
                else:
                    break
        return res
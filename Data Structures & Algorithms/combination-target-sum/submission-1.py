class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        combos = []
        newcombos = [[]]
        res = []
        while newcombos:
            combos = newcombos
            newcombos = []
            for i in range(len(combos)):
                for k in nums:
                    if len(combos[i]) > 0 and k < combos[i][-1]:
                        continue
                    newtotal = sum(combos[i]) + k
                    if newtotal == target:
                        res.append(combos[i] + [k])
                    elif newtotal < target:
                        newcombos.append(combos[i] + [k])
                    
        return res



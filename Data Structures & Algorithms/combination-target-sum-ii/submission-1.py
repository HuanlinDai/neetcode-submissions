class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combos = [[]]
        newcombos = []
        res = []
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                combos += newcombos
                morecombos = []
                for combo in newcombos:
                    total = sum(combo) + candidates[i]
                    if total == target:
                        res.append(combo + [candidates[i]])
                    elif total < target:
                        morecombos.append(combo + [candidates[i]])
                newcombos = morecombos
            else:
                combos += newcombos
                newcombos = []
                for combo in combos:
                    total = sum(combo) + candidates[i]
                    if total == target:
                        res.append(combo + [candidates[i]])
                    elif total < target:
                        newcombos.append(combo + [candidates[i]])
        return res

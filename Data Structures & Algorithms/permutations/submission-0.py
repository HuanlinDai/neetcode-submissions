class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        combos = [[]]
        newcombos = []
        for _ in range(len(nums)):
            for combo in combos:
                for k in nums:
                    if not k in combo:
                        newcombos.append(combo + [k])
            combos = newcombos
            newcombos = []

        return combos
                
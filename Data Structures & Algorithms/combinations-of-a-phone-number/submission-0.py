class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combos = ['']
        keys = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        for i in range(len(digits)):
            newcombos = []
            for c in keys[digits[i]]:
                for combo in combos:
                    newcombos.append(combo + c)
            combos = newcombos

        return combos
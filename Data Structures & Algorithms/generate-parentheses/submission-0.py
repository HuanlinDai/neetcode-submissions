class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        combos = [(0,"")]
        for _ in range(2*n):
            newcombos = []
            for kopen, s in combos:
                if kopen < n:
                    newcombos.append((kopen + 1, s + "("))
                if 2*kopen > len(s):
                    newcombos.append((kopen, s + ")"))
            combos = newcombos
        
        return [combo[1] for combo in combos]
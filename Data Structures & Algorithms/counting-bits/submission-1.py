class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(Counter(bin(i))['1'])
        return res
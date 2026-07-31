class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            numones = 0
            dig = i
            while dig:
                numones += dig & 1
                dig >>= 1
            res.append(numones)

        return res
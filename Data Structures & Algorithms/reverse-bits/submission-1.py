class Solution:
    def reverseBits(self, n: int) -> int:
        bs = bin(n)[::-1][:-2]
        bs = bs + '0' * (32 - len(bs))
        return int(bs, 2)
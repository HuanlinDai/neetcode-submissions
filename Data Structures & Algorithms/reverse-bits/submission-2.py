class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:][::-1]
        return int('0b' + s + ''.join(['0'] * (32-len(s))), 2)
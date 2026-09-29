class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        freqs = [1] + [0] * amount
        for c in sorted(coins):
            for i in range(len(freqs)):
                if i + c <= amount:
                    freqs[i+c] += freqs[i]
        return freqs[-1]
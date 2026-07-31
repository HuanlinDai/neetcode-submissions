class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        twobefore = 1
        onebefore = 2
        for i in range(n-2):
            twobefore, onebefore = onebefore, twobefore + onebefore
        return onebefore
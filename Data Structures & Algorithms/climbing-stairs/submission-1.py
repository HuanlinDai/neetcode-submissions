class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        twobefore = 1
        onebefore = 2
        for i in range(2,n):
            now = twobefore + onebefore
            twobefore = onebefore
            onebefore = now
        return now
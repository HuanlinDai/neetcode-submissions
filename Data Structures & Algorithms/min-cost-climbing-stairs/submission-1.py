class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        twobefore = cost[0]
        onebefore = cost[1]

        for i in range(2,n):
            twobefore, onebefore = onebefore, min(twobefore, onebefore) + cost[i]
        
        return min(twobefore, onebefore)
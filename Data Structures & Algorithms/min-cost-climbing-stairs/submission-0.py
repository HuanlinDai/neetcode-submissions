class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        twobefore = cost[0]
        onebefore = cost[1]

        for i in range(2,len(cost)):
            now = cost[i] + min(twobefore, onebefore)
            twobefore = onebefore
            onebefore = now
        
        return min(twobefore, onebefore)
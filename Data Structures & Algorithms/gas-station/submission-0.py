class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = 0
        n = len(gas)
        curgas = 0
        for r in range(2*len(gas)-1):
            curgas += gas[r%n] - cost[r%n]
            while l <= r and curgas < 0:
                curgas -= gas[l%n] - cost[l%n]
                l += 1
            if r - l + 1 == n:
                return l
        return -1
            
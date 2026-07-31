class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        

        n = len(stones)
        total = sum(stones)
        dp = set([total//2])
        
        done = set()
        for i in range(n):
            newdp = dp.copy()
            for subtotal in dp:
                newtotal = subtotal-stones[i]
                if newtotal == 0:
                    return total - 2*(total//2)
                elif newtotal > 0:
                    newdp.add(newtotal)
            dp = newdp

        return 2*min(dp) + (total%2)
        



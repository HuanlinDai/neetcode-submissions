class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = sum(piles)
        lastvalid = r
        while l <= r:
            k = (l+r)//2
            time = 0

            for pile in piles:
                time += math.ceil(pile/k)
            if time > h:
                l = k + 1
            else:
                lastvalid = k
                r = k - 1
        return lastvalid

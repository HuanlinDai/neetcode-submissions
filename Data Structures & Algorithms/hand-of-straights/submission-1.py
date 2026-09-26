class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freqs = Counter(hand)
        keys = sorted(freqs.keys())
        for cur in keys:
            while freqs[cur] > 0:
                for key in range(cur, cur+groupSize):
                    if freqs.get(key,0) == 0:
                        return False
                    freqs[key] -= 1
            
        return True
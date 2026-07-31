class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        res = [False, False, False]
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                res[0] = res[0] or a == target[0]
                res[1] = res[1] or b == target[1]
                res[2] = res[2] or c == target[2]
            
        return res[0] and res[1] and res[2]
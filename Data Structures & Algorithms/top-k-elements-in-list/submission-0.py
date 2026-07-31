class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] += 1
        freqlists = {}
        for num in freqs:
            if freqs[num] not in freqlists:
                freqlists[freqs[num]] = [num]
            else:
                freqlists[freqs[num]].append(num)
        res = []
        ordered_freqs = sorted(freqlists.keys(), reverse=True)
        for freq in ordered_freqs:
            res += freqlists[freq]
            if len(res) >= k:
                return res
        return res

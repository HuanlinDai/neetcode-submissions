class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for i in nums:
            freqs[i] = freqs.get(i,0) + 1
        freqfreqs = {}
        for i in freqs:
            if freqs[i] in freqfreqs:
                freqfreqs[freqs[i]].append(i)
            else:
                freqfreqs[freqs[i]] = [i]
        res = []
        sorted_freqs = sorted(freqfreqs.keys(), reverse = True)
        while len(res) < k:
            mostfreq = sorted_freqs.pop(0)
            res += freqfreqs[mostfreq]
        return res
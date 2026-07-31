class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freqs = Counter(nums)
        freqtodigs = {}
        for i in freqs:
            freqtodigs[freqs[i]] = freqtodigs.get(freqs[i], []) + [i]
        for freq in sorted(freqtodigs.keys(), reverse = True):
            res += freqtodigs[freq]
            if len(res) >= k:
                break
        return res
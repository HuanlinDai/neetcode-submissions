class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        freqs2 = Counter(freqs.values())
        nummax = freqs2[max(freqs2)]
        return max((n+1) * (max(freqs2) - 1) + nummax, len(tasks))

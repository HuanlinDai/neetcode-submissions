class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        inds = {}
        for i in range(len(s)):
            if s[i] not in inds or (s[i] in inds and inds[s[i]] == -1):
                longest = max(longest, i-start+1)
            else:
                while start <= inds[s[i]]:
                    inds[s[start]] = -1
                    start += 1
            inds[s[i]] = i
        return longest
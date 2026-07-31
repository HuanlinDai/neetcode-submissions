class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set({})
        res = 0
        last = 0
        for i in range(len(s)):
            if s[i] in seen:
                while s[i] in seen:
                    seen.remove(s[last])
                    last += 1
                seen.add(s[i])
            else:
                seen.add(s[i])
                res = max(res, i-last+1)
        return res
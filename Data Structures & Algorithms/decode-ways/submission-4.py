class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dps = [1,1]
        for i in range(1,len(s)):
            dp = dps[i]
            if s[i] == "0":
                if s[i-1] not in "12":
                    return 0
                dp = dps[i-1]
            elif s[i-1] == "1" or (s[i-1] == "2" and s[i] in "123456"):
                dp += dps[i-1]
            dps.append(dp)

        return dps[-1]
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # dp problem because let's say we choose a character that doesn't match at some index in s. then, the rest of the string
        # might not match, so we have to consider subproblems

        # if we have just the ".", we can match lengths and we don't need dp. the "*" is what makes it difficult.
        # if there is a "*", we need to know what letter we're repeating. if it's a specific letter, we need
        

        # what does the brute force look like?
        # for every letter, try to match it.
        # for every ".", continue
        # for every "*",
            # try every length possible of that letter - would look like dfs for future decisions
            # O(n) letters we might start the dfs from and each decision with * is O(2^n) which is v bad!!!
       
        # this dfs might be able to benefit from dp memoization
        # what should the dp memos represent? if the rest of the string matched
        # 

        m, n = len(s), len(p)
        dp = {}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i >= m and j >= n:
                return True
            elif j >= n:
                return False
            
            match = i < m and (s[i] == p[j] or p[j] == ".")
            if j < n-1 and p[j+1] == "*":
                dp[(i,j)] = dfs(i, j+2) or (match and dfs(i+1,j))
                return dp[(i,j)]
            if match:
                dp[(i,j)] = dfs(i+1, j+1)
                return dp[(i,j)]
            dp[(i,j)] = False
            return False

        return dfs(0,0)
class Solution:
    def trap(self, height: List[int]) -> int:
        prefixmax = [0]
        postfixmax = [0]
        n = len(height)
        for i in range(n-1):
            prefixmax.append(max(prefixmax[-1], height[i]))
            postfixmax.append(max(postfixmax[-1], height[n-i-1]))
        postfixmax.reverse()
        res = 0
        for i in range(n):
            if height[i] < min(prefixmax[i], postfixmax[i]):
                res += min(prefixmax[i], postfixmax[i]) - height[i]
        return res

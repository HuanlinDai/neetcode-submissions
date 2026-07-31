class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        res = 0
        stack = []
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                ind, height = stack.pop(-1)
                res = max(res, height * (i - ind))
                start = ind
            stack.append((start,heights[i]))
        
        for ind, height in stack:
            res = max(res, height * (len(heights) - ind))

        return res
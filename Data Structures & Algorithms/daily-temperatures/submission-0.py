class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        stack = [(temperatures[0],0)]

        for i in range(1,n):
            while stack and stack[-1][0] < temperatures[i]:
                _,ind = stack.pop(-1)
                res[ind] = i - ind
            stack.append((temperatures[i],i))
        
        return res
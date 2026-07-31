class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]
        postfix = [1]
        for i in range(n-1):
            prefix.append(prefix[i] * nums[i])
            postfix.append(postfix[i] * nums[n-i-1])
        postfix = postfix[::-1]
        return [prefix[i] * postfix[i] for i in range(n)]
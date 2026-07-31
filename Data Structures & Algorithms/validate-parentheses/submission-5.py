class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            elif s[i] == ")" and stack[-1] != "(" or \
                 s[i] == "]" and stack[-1] != "[" or \
                 s[i] == "}" and stack[-1] != "{":
                return False
            else:
                stack.pop(-1)
        return len(stack) == 0
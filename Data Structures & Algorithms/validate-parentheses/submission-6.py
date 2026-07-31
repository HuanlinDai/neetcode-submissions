class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            elif not stack:
                return False
            else:
                bracket = stack.pop(-1)
                if bracket != "(" and s[i] == ")" or \
                   bracket != "[" and s[i] == "]" or \
                   bracket != "{" and s[i] == "}":
                   return False
        return len(stack) == 0
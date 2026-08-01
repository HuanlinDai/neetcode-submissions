class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ('(', '[', '{'):
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                cand = stack.pop(-1)
                if cand == '(' and s[i] != ')' or \
                    cand == '[' and s[i] != ']' or \
                    cand == '{' and s[i] != '}':
                    return False

        return len(stack) == 0
                    
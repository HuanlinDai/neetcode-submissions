class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in {"[", "(", "{"}:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                last = stack.pop(-1)
                if last == "[" and s[i] != "]":
                    return False
                elif last == "(" and s[i] != ")":
                    return False
                elif last == "{" and s[i] != "}":
                    return False
        if stack:
            return False
        return True
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        stack = []
        inds = {}

        for i in range(len(s)):
            stack.append(s[i])
            if s[i] in inds:
                # start collapsing
                while len(stack) > inds[s[i]] + 1:
                    stack[inds[s[i]]] += stack.pop(inds[s[i]] + 1)
                for c in stack[inds[s[i]]]:
                    inds[c] = len(stack) - 1
            else:
                inds[s[i]] = len(stack) - 1

                

        return [len(ss) for ss in stack]
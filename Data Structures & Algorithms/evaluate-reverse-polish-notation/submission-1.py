class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in range(len(tokens)):

            if tokens[i] == "+":
                b = stack.pop(-1)
                a = stack.pop(-1)
                stack.append(a + b)
            elif tokens[i] == "-":
                b = stack.pop(-1)
                a = stack.pop(-1)
                stack.append(a - b)
            elif tokens[i] == "*":
                b = stack.pop(-1)
                a = stack.pop(-1)
                stack.append(a * b)
            elif tokens[i] == "/":
                b = stack.pop(-1)
                a = stack.pop(-1)
                stack.append(int(a / b))
            else:
                stack.append(int(tokens[i]))
        return stack[0]
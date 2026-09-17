class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                sum_value = stack[-1] + stack[-2]
                stack.pop()
                stack.pop() 
                stack.append(sum_value)
            elif token == "*":
                mult_value = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(mult_value)
            elif token == "-":
                minus_value = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(minus_value)
            elif token == "/":
                division_value = int(stack[-2]/stack[-1])
                stack.pop()
                stack.pop()
                stack.append(division_value)
            else:
                stack.append(int(token))

        return stack[0]
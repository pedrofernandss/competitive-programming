class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total_sum = 0
        stack = []

        for operation in operations:                
            if operation == "D":
                value = 2*int(stack[-1])
                total_sum += value
                stack.append(value)
            elif operation == "C":
                total_sum -= stack[-1]
                stack.pop()
            elif operation == "+":
                curr_sum = stack[-1] + stack[-2]
                total_sum += curr_sum
                stack.append(curr_sum)                
            else:
                total_sum += int(operation)
                stack.append(int(operation))

        return total_sum
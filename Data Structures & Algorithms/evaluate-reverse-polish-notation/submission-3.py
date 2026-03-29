class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                second = stack.pop()
                first = stack.pop()
                result = first + second
                stack.append(result)
            elif char == "-":
                second = stack.pop()
                first = stack.pop()
                result = first - second
                stack.append(result)
            elif char == "*":
                second = stack.pop()
                first = stack.pop()
                result = first * second
                stack.append(result)
            elif char == "/":
                second = stack.pop()
                first = stack.pop()
                result = int(first / second)
                stack.append(result)
            else:
                stack.append(int(char))
        return stack.pop()
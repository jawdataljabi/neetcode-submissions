class Solution:
    def isValid(self, s: str) -> bool:
        stack = list(s)
        complement = {"(": ")", "{": "}", "[": "]"}

        if len(s) % 2 != 0:
            return False

        for index, char in enumerate(stack):
            if char not in complement:
                return False
            elif complement[char] == stack[-1]:
                stack.pop()
            elif complement[char] == stack[index + 1]:
                del stack[index + 1]
            else:
                return False
        return True

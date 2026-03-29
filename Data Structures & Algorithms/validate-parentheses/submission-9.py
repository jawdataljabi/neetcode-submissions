class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        complement = {"(": ")", "{": "}", "[": "]"}

        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in complement:
                stack.append(char)
            else:
                if not stack:
                    return False
                opening = stack.pop() # get the right most opening element in stack which was added earlier
                if complement[opening] != char:
                    return False
        return not stack


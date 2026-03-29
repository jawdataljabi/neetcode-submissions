class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        lookup = {"]": "[", "}": "{", ")": "("}

        for bracket in s:
            if bracket == "[":
                stack.append("[")
            elif bracket == "(":
                stack.append("(")
            elif bracket == "{":
                stack.append("{")
            else: # pop the top and check if it is equal to corresponding bracket
                if not stack:
                    return False
                top = stack.pop()
                if top != lookup[bracket]:
                    return False
        
        return not stack
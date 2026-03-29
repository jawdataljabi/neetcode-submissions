class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        outer = inner = n # for the parentheses
        output = []
        stack = []

        # ["("], n = 2

        def dfs(stack, outer, inner):
            if inner == outer == 0:
                output.append("".join(stack))
                return
            
            if inner > outer: # inner = 2, outer = 1
                stack.append(")")
                dfs(stack, outer, inner - 1)
                stack.pop()
            if outer > 0:
                stack.append("(")
                dfs(stack, outer - 1, inner)
                stack.pop()
        
        dfs(stack, outer, inner)
        return output

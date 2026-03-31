class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        subset = []
        outer = inner = n # this indicates how many of brackets each we have left

        def dfs(outer, inner):
            if inner == outer == 0:
                output.append("".join(subset))
                return
            
            if inner > outer:
                subset.append(")")
                dfs(outer, inner - 1)
                subset.pop()
            if outer > 0:
                subset.append("(")
                dfs(outer - 1, inner)
                subset.pop()
            
        dfs(n, n)
        return output

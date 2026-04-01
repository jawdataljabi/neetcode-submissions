class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        counter = 0
        adjList = []

        for _ in range(n):
            adjList.append([])

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)
            for neighbor in adjList[node]:
                dfs(neighbor)

        
        for node in range(n):
            if node not in seen:
                dfs(node)
                counter += 1
        

        return counter


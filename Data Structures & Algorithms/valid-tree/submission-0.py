class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        adjList = []
        
        for _ in range(n):
            adjList.append([])

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
            
        #     0       1     2    3    4
        # [[1,2,3], [0,4], [0], [0], [1]] = adjList

        # seen = {0,1,2}
        # 0 <-> 1 <-> 2
        # prev = 1

        def dfs(node, prev):
            # base case
            if node in seen:
                return False
            
            seen.add(node)
            for neighbor in adjList[node]:
                if neighbor == prev:
                    continue
                elif not dfs(neighbor, node):
                    return False
            return True
                

        return dfs(0, -1) and len(seen) == n

        
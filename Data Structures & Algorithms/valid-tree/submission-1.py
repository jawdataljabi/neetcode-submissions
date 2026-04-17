class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # for a tree to be valid:
        # 1) no cycles 
        # 2) no disconnets (no lonely nodes)
        
        # first we can create an adjList which would show all the connections for nodes
        # [[1,2,3], [0,4], ...]

        # second, we can implement dfs(node, prev); for each node, check it's neighbors to check for any cycles

        # at the very end, check is length of the set is equal to n; if not, then return False

        adjList = []

        for _ in range(n):
            adjList.append([])

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        # by now, adjList has been properly created

        seen = set()

        def dfs(node, prev):
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
                

            




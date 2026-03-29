"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # for every node, check it's neighbours: add it to hash map -> then if neighbour is not inside of hash map,
        # then add it to the hashmap and run the function on it -> otherwise if it is already in the hash map, then connect edge to it
        # (add it as a neighbour)
        if not node:
            return None

        oldToNew = {} # {oldNode: newNode}

        def traversal(node): # bfs
            queue = deque()
            newNode = Node(node.val)
            oldToNew[node] = newNode
            queue.append(node)

            while queue:
                node = queue.popleft()
                for neighbour in node.neighbors:
                    if neighbour not in oldToNew:
                        oldToNew[neighbour] = Node(neighbour.val)
                        queue.append(neighbour)

                    newNode = oldToNew[node]
                    newNode.neighbors.append(oldToNew[neighbour])
            
        traversal(node)
        return oldToNew[node]


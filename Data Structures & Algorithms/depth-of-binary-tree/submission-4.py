# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # SOLUTION 1: (DFS recursively)
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


        # SOLUTION 2: (DFS iteratively)
        if not root:
            return 0

        result = 1
        stack = [[root, 1]]

        while stack:
            for i in range(len(stack)):
                node, depth = stack.pop()
                if node.left:
                    stack.append([node.left, depth + 1])
                    result = max(result, depth + 1)
                if node.right:
                    stack.append([node.right, depth + 1])
                    result = max(result, depth + 1)

        return result
            

        

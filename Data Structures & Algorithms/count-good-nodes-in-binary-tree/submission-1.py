# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.output = 0
        
        def dfs(root, maxValue):
            if not root:
                return 
            
            if root.val >= maxValue:
                self.output += 1
                maxValue = root.val
            
            left = dfs(root.left, maxValue)
            right = dfs(root.right, maxValue)

            return
        
        dfs(root, root.val)
        return self.output
            


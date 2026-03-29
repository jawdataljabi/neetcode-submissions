# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        elif not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



    # helper function
    def isSameTree(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1:
            return False
        elif not node2:
            return False
        elif node1.val != node2.val:
            return False
        
        left = self.isSameTree(node1.left, node2.left)
        right = self.isSameTree(node1.right, node2.right)

        return left and right

        
        
        
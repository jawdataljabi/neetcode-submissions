# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # process is to use dfs to add the heights bottom up, and for each
        # node check whether it is not balanced or not by using a boolean

        def dfs(root):
            if not root:
                return [True, 0] # this should occur at a leaf

            left = dfs(root.left)
            right = dfs(root.right)

            # means that it is not balanced, so return False
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])] 
        
        return dfs(root)[0] # will return the boolean
        print("hello world!")

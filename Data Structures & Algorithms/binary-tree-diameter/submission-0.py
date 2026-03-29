# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        # We want to return the height, not the diameter here
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            self.result = max(self.result, left + right) # adding left and right since that gives the diameter

            # Returning the height so it could be used as part of the diameter calc for the very first node called
            return 1 + max(right, left) 
        
        dfs(root)
        return self.result

            









































        # # idea is to take the max children of each node
        # def dfs(root, result):
        #     if not root: # if leaf
        #         return 0
            
        #     left = dfs(root.left, 1 + result)
        #     right = dfs(root.right, 1 + result)

        #     return left + right

        # return dfs(root, 0) 

        # print("hello world!")
        # print("you are trash - andrea")
            
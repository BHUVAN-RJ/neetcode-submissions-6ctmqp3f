# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0

        def get_diameter(node):
            if not node:
                return 0
            
            left = get_diameter(node.left)
            right = get_diameter(node.right) 
            
            self.dia = max(self.dia, left + right)
            return max(left, right) + 1
        
        get_diameter(root)
        return self.dia

            

        
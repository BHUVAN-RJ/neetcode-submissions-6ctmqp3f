# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        dummy = root

        def insert(root, node):
            if root.val >= node.val:
                if root.left:
                    return insert(root.left, node)
                else:
                    root.left = node
                    return root
                
            else:
                if root.right:
                    return insert(root.right, node)
                else:
                    root.right = node
                    return root
        
        node = TreeNode(val)
        if root :
            insert(root, node)
        else:
            return node
        return dummy
        

        
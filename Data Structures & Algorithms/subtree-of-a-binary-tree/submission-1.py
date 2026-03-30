# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.subTreeStart(root, subRoot)

    def subTreeStart(self, root, subroot):
        if not root:
            return False
        
        if root.val == subroot.val:
            res = self.subTreeCheck(root, subroot)
            if res:
                return res
        left = self.subTreeStart(root.left, subroot)
        right = self.subTreeStart(root.right, subroot)

        return (left or right)
    
    def subTreeCheck(self, root, subroot):
        if not root and not subroot:
            return True
        
        if root and not subroot:
            return False
        
        if subroot and not root:
            return False

        if root.val != subroot.val:
            return False

        left = self.subTreeCheck(root.left, subroot.left)
        right = self.subTreeCheck(root.right, subroot.right)

        return (left and right)
    
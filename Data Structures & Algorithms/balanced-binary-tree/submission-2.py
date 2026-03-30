# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        left, lbalanced = self.getHeight(root.left)
        right, rbalanced = self.getHeight(root.right)
        if abs(left-right) <= 1 and lbalanced and rbalanced:
            return True
        return False
    def getHeight(self, root):
        if not root: return 0, True
        print(self.getHeight(root.left))

        left, lbalanced = self.getHeight(root.left)
        right, rbalanced = self.getHeight(root.right)

        balanced = True if abs(left-right) <=1 else False

        return 1 + max(left, right), bool((balanced and lbalanced and rbalanced))

        
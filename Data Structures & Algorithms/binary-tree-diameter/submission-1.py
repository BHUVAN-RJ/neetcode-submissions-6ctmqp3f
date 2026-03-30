# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        length, res = self.getDiameter(root, 0)
        return res

    
    def getDiameter(self, root, curMax):
        if not root: return 0, curMax

        left, curMax = self.getDiameter(root.left, curMax)
        right, curMax = self.getDiameter(root.right, curMax)

        curMax = max(curMax, (left + right))

        return 1 + max(left, right), curMax
        
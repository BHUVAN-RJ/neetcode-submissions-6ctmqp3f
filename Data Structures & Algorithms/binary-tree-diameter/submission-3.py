# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getDiameter(node, diameter):
            if not node:
                return 0, 0
            curL = curR = 0
            curLdia = curRdia = 0
            if node.left:
                curLdia, curL = getDiameter(node.left, diameter)
            if node.right:
                curRdia, curR =  getDiameter(node.right, diameter)
            
            cur = curL + curR
            diameter = max(diameter, cur, curRdia, curLdia)
            return diameter, 1 + max(curL, curR)
        return getDiameter(root, 0)[0]
        
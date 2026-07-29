# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root

        def splitDetect(parent):
            print(parent.val)
            if (p.val <= parent.val and q.val >= parent.val) or (q.val <= parent.val and p.val >= parent.val):
                res = parent
                print('res changed')
                return parent
            elif p.val < parent.val and q.val < parent.val:
                return splitDetect(parent.left)
            else:
                return splitDetect(parent.right)
        res = splitDetect(root)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''

 preorder = [1,2,3,4]
 inorder = [2,1,3,4]

'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexes = {val:i for i,val in enumerate(inorder)}
        self.pre_root = 0

        def dfs(left, right):
            if left > right:
                return None
            node = TreeNode(preorder[self.pre_root])
            mid = indexes[node.val]
            self.pre_root += 1
            node.left = dfs(left, mid - 1)
            node.right = dfs(mid + 1, right)
            return node
        
        return dfs(0, len(preorder) - 1)

        
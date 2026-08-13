# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
we need a sorted list of numbers - the binary tree rule is that the left subtree
will always have children less than the parent
so for every subtree if we build the res list by travellling left root node - preorder traversal
we will have a list that will be sorted 
   4


'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inorder(node):
            if not node:
                return
            
            if node.left:
                inorder(node.left)
            res.append(node.val)
            if node.right:
                inorder(node.right)
            return 
        inorder(root)
        return res[k - 1]
        
        print(res)




        
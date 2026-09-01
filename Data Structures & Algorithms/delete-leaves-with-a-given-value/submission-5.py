# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
just keep deleting if val == taarget

pseudo:
base case -> if not valid node -> return
left = true
right = true
if left or right -> del that node

if leaf node 
-> yes -> check ==? val -> if yes -> return true else false
-> no -> return





'''
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):# 1
            if not node:
                return False
            
            left = dfs(node.left)#1 -> false
            right = dfs(node.right)#1 right -> false

            if left:
                node.left = None
            if right:
                node.right = None
            
            if node.left or node.right:#not leaf node
                return False
            else:#leaf node
                if node.val == target:
                    return True
                else:
                    return False
        res = dfs(root)
        return None if res else root

        
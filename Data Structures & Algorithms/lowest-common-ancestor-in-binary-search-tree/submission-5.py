# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
case 1: main root is commman ancestor
INput - [5,3,8,1,4,7,9,null,2]
dfs()
parents =        [5]
            [5,3]   [5,8]
    [5,3,1].  [5,3,4][5,8,7] [5,8,9]
         [5,3,1,2]

stack = []

parent_list1 = [5,8,7]
parent_list2 = [5,3,1,2]
                      i
n nodes - n lists
space = O(2^n)
time = O(n)

res = None


somehow globallys tore these lists of parents

dfs = [5, 8, 7]
dfs = [5, 3, 1, 2]


case 2: both nodes in left or right
dfs = [5,3,4]
dfs = [5,3,1,2]



if both on same side or not - 



'''
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lst1 = []
        self.lst2 = []

        def dfs(root, parents):
            if not root:
                return 
            parents.append(root)
            if root == p:
                self.lst1 = parents.copy()
            elif root == q:
                self.lst2 = parents.copy()
            dfs(root.left, parents.copy())
            dfs(root.right, parents.copy())
        
        dfs(root,[])
        length = min(len(self.lst1), len(self.lst2))
        i = 0
        res = None


        while i < length:
            if self.lst1[i].val == self.lst2[i].val:
                res = self.lst1[i]
            i += 1
        return res

        




        










        
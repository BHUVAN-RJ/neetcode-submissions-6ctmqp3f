# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
every level only one node is visible 
first go to right, if right is present then add and go to next level else check the left node

[3, 2]
'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        q = collections.deque()
        if root:
            q.append(root) #[1, 3, 4, 5]

        while True: # [null, null]
            qLen = len(q) # 
            if not qLen:
                break
            level = 1
            for i in range(qLen): # 
                node = q.popleft() # 
                if node:
                    if level > 0: # T
                        res.append(node.val)
                        level -= 1
                    q.append(node.right)
                    q.append(node.left)
        
        return res

                



            
            


        
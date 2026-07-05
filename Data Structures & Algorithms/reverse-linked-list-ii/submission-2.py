# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
IN: LL, left and right - left always <= right
OUT: head on the LL
GOAL: reverse the elements from left to right,
Facts:
-> left and right are 1 indexed not 0
-> left = right = n(number of elements)
-> if l == r - we can just return caz no reversal

1 -> 2 -> 3 -> 4 -> 5
C    L    R

2 -> 3 -> 1 -> 4 -> 5
C    LR

3 -> 2 -> 1 -> 4 -> 5
LR (BREAK)


1 -> 2 -> 3 -> none
CL         R

2 -> 3 -> 1 -> none


1 -> 4 -> 3 -> 2 -> 5
     L    R


Intuition:
We can have 2 heads L and R and the remove the nodes from L 
attach them as the next nodes to R
return when L = R

works
edge cases:
L==R -> handled -> directly breaks and returns
R = N -> works handle the next = none case seperately if needed
when L > 1 -> handle the cases of correctly pointing the left
to the next element



left = 1
1 -> 3 -> 4 -> 2 -> 5 -> 6
P    C.   LR
while left:


'''

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lHead = head
        rHead = head
        prev = ListNode(0, lHead)
        retType = None
        if left == 1:
            retType = 'rHead'
        while left > 1:
            prev = lHead
            lHead = lHead.next
            left -= 1
            
        
        while right > 1:
            rHead = rHead.next
            right -= 1
        # 0 -> 3 -> 2 -> 1 -> 4 -> 5( left = 1, right = 3)
        # p    LR           
        # we have the left head and right head in positions
        while lHead != rHead:
            cur = lHead
            lHead = lHead.next
            # delete the node
            prev.next = lHead


            # add the node to the end
            tmp = rHead.next
            rHead.next = cur
            cur.next = tmp
        
        # return cases - rHead if l == 1 else
        return rHead if retType == 'rHead' else head
        




        
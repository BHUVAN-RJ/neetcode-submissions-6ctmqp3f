# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next = None
        newHead = None
        while head:
            curNode = ListNode(head.val)
            if next:
                curNode.next = next
            next = curNode
            head = head.next
            if not head:
                newHead = curNode
        return newHead
        
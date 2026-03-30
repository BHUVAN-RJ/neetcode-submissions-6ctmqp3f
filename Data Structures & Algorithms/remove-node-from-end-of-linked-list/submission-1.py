# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        newHead = head
        while newHead:
            length += 1
            newHead = newHead.next

        nodeNum = length - n 
        num = 1
        prev = None
        newHead = head
        while num < nodeNum:
            prev = newHead
            newHead = newHead.next
            num += 1


        if not prev:
            return newHead.next
        prev.next = newHead.next
        return head

        
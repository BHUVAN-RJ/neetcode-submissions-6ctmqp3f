# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        reminder = 0
        head = None
        while l1 and l2:
            curSum = l1.val + l2.val + reminder
            if curSum >= 10:
                curSum -= 10
                reminder = 1
            else:
                reminder = 0
            curDigitNode = ListNode(curSum)

            l1 = l1.next
            l2 = l2.next
            if prevNode:
                prevNode.next = curDigitNode
            else:
                head = curDigitNode
            prevNode = curDigitNode

        if l1:
            while l1:
                curSum = l1.val + reminder
                if curSum >= 10:
                    curSum -= 10
                    reminder = 1
                else:
                    reminder = 0
                curNode = ListNode(curSum)
                prevNode.next = curNode
                l1 = l1.next
                prevNode = curNode
        elif l2:
            while l2:
                curSum = l2.val + reminder
                if curSum >= 10:
                    curSum -= 10
                    reminder = 1
                else:
                    reminder = 0
                curNode = ListNode(curSum)
                prevNode.next = curNode
                l2 = l2.next
                prevNode = curNode

        if reminder:
            prevNode.next = ListNode(1)
        
        return head


        
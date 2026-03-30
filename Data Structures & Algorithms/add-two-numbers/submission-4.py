# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 975 = 5->7->9
        #  67 = 7->6
        carry = 0
        head = ListNode()
        cur_node = head
        while l1 or l2:
            if l1 and l2:
                cur_val = l1.val + l2.val
                if carry > 0:
                    cur_val += carry
                    carry -= 1
                l1 = l1.next
                l2 = l2.next
            elif l1:
                if carry > 0:
                    cur_val = l1.val + carry
                    carry -= 1
                else:
                    cur_val = l1.val
                l1 = l1.next
            elif l2:
                if carry > 0:
                    cur_val = l2.val + carry
                    carry -= 1
                else:
                    cur_val = l2.val
                l2 = l2.next
            if cur_val > 9:
                carry = 1
                cur_val -= 10
            else:
                carry = 0
            node = ListNode(cur_val)
            cur_node.next = node
            cur_node = node
        if carry > 0:
            cur_node.next = ListNode(1)
        return head.next
            


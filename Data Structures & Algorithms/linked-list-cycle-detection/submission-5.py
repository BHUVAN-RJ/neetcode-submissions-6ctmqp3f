# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# hare and tortise algo
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h, t = head, head

        while h:
            if h.next:
                h = h.next.next
            else:
                break
            t = t.next
            if h == t:
                return True

        return False

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #check if heads exist and which is smaller -> then loop until atleast 
        res = None
        resHead = None 
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    if not res:
                        res = list1
                        list1 = list1.next
                        resHead = res
                        continue
                    res.next = list1
                    res = res.next
                    list1 = list1.next
                else:
                    if not res:
                        res = list2
                        list2 = list2.next
                        resHead = res
                        continue
                    res.next = list2
                    res = res.next
                    list2 = list2.next
            elif list1:
                if not res:
                        res = list1
                        list1 = list1.next
                        resHead = res
                        continue
                res.next = list1
                list1 = list1.next
                res = res.next
            else:
                if not res:
                        res = list2
                        list2 = list2.next
                        resHead = res
                        continue
                res.next = list2
                list2 = list2.next
                res = res.next
        return resHead


        
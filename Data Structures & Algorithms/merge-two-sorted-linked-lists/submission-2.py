# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
# input: two heads of sorted LLs
# output: one head for a sorted LL that merges both the sorted lists
# goal: merge both the sorted lists so that they stay sorted
# facts:
1. should just merge the two LLs, not create new one( as in done create nodes just use the ones already there)
2. there can be repeated values for nodes in each list
3. there can be null values( no elements in one or both lists)
4. node val can be negative

# assumptions:
1. I can create a few nodes

1 -> 2 -> 4 -> null
            h1
1 -> 3 -> 5 -> null
          h2

1 -> 1 -> 2 -> 3 -> 4 -> null
h
# approach:
while h1 and h2:
compare h1 and h2 -> whichever smaller - put it to h

whiile h1:
complete the rest of the LL

while h2:
    complete the rest of the LL


    
# complexity:
O(n + m)
O(1)
    '''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        newList = head
        while list1 and list2:
            if list1.val <= list2.val:
                newList.next = list1
                list1 = list1.next
            else:
                newList.next = list2
                list2 = list2.next
            newList = newList.next
        
        while list1:
            newList.next = list1
            list1 = list1.next
            newList = newList.next
        
        
        while list2:
            newList.next = list2
            list2 = list2.next
            newList = newList.next
        
        return head.next
        


        
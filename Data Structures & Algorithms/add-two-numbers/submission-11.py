# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
IN: 2 LL each representing a number
OUT: one LL representing the answer
add the two LL and then returen the result as an LL
Questions:
1. what if the first number is shorter than the second -> easily can handle
2. how to carry over --> max can be 1

DRY RUN:
ONE:  1 -> 2 -> 3 (321)
TWO:  4 -> 5 -> 6 (654)
RES:  5 -> 7 -> 9

edge 1:
9 -> 9
9 -> 9
8 -> 9 -> 1

edge 2:
1 -> 2 -> 3 -> 4
5 -> 6 -> 7
6 -> 8 -> 0 -> 5 

Solution:
iterate through each node - add both, store carry.
dummy head = node
curhead = dummy
while h1 and h2:
    cursum = h1+h2
    if cursum > 9:
        carry = T
        cursum -= 9
    
    new node = listnode(cursum)
    curhead.next = new
    curhead = curhead.next
    h1 = h1.next

'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curHead = dummy
        carry = False
        while l1 and l2:
            cursum = l1.val + l2.val
            if carry:
                cursum += 1
                carry = False
            if cursum > 9:
                carry = True
                cursum %= 10
            
            newNode = ListNode(cursum)
            curHead.next = newNode
            curHead = curHead.next
            l1 = l1.next
            l2 = l2.next
                
        
        while l1:
            if carry:
                l1.val += 1
                carry = False
                if l1.val > 9:
                    l1.val %= 10
                    carry = True
            print(curHead.val)
            curHead.next = l1
            curHead = curHead.next
            l1 = l1.next

        while l2:
            if carry:
                l2.val += 1
                carry = False
                if l2.val > 9:
                    l2.val %= 10
                    carry = True
            curHead.next = l2
            curHead = curHead.next
            l2 = l2.next
            
        
        
        
        if carry:
            newNode = ListNode(1)
            print("YES")
            while curHead.next:
                curHead = curHead.next
            
            curHead.next = newNode

        dum2 = dummy.next
        while dum2:
            print(dum2.val)
            dum2 = dum2.next
        return dummy.next





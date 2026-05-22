
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.store = [[ListNode(None)] for i in range(10000)]
        
        

    def add(self, key: int) -> None:
        idx = key % 10000
        head = self.store[idx][0]
        while head.next:
            if head.next.val == key:
                return
            head = head.next
        head.next = ListNode(key)
        
        

    def remove(self, key: int) -> None:
        idx = key % 10000
        head = self.store[idx][0]
        prev = head
        while head.next:
            if head.next.val == key:
                head.next = head.next.next
                return
            head = head.next

    def contains(self, key: int) -> bool:
        idx = key % 10000
        head = self.store[idx][0]
        while head.next:
            if head.next.val == key:
                return True
            head = head.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10000)]

    def add(self, key: int) -> None:
            head = self.set[key%10000]
            while head:
                if head.key == key:
                    return
                elif head.next == None:
                    head.next = ListNode(key)
                else:
                    head = head.next
                


        

    def remove(self, key: int) -> None:
        if self.set[key%10000]:
            head = self.set[key%10000]
            prev = None
            while head:
                if head.key == key:
                    if prev == None:
                        self.set[key%10000] = self.set[key%10000].next
                    else:
                        prev.next = head.next
                    return
                elif head.next == None:
                    break
                else:
                    prev = head
                    head = head.next
                    

        

    def contains(self, key: int) -> bool:
        if self.set[key%10000]:
            head = self.set[key%10000].next
            while head:
                if head.key == key:
                    return True
                elif head.next == None:
                    break
                else:
                    head = head.next
        return False
            
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
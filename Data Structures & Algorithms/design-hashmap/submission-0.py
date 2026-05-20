class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.map = [ListNode(None, None) for i in range(1000)]
        

    def put(self, key: int, value: int) -> None:
        head = self.map[key%1000]

        while head.next:
            if head.next.key == key:
                head.next.value = value
                return
            head = head.next
        head.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        head = self.map[key%1000]

        while head.next:
            print(f"GET:{head.key}",head.value)
            if head.next.key == key:
                return head.next.value
            head = head.next
        return -1
        

    def remove(self, key: int) -> None:
        head = self.map[key%1000]

        while head.next:                
            if head.next.key == key:
                head.next = head.next.next
                return
            head = head.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
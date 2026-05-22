class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashmap = [[ListNode(None, None)] for i in range(10000)]
        

    def put(self, key: int, value: int) -> None:
        head = self.hashmap[key % 10000][0]
        while head.next:
            if head.next.key == key:
                head.next.val = value
                return
            head = head.next
        head.next = ListNode(key,value)
        

    def get(self, key: int) -> int:
        head = self.hashmap[key % 10000][0]
        while head.next:
            if head.next.key == key:
                return head.next.val
            head = head.next
        return -1
        

    def remove(self, key: int) -> None:
        head = self.hashmap[key % 10000][0]
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
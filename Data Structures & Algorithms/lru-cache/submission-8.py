'''
in: key / key-value / capacity
out: get - return the value for the key if key exists - else return -1
    put - update value if ke exists, else add the val,key to the cache 
    - if val greater than capacity remove the least recently used
goal: update the cache - if get/put is used on an element it is considered used

(least recently used)l <-> 2 <-> r( recently used)
'''

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cap = capacity
        self.length = 0
        self.cache = {}
    
    def insert(self, node):
        temp = self.right.prev
        self.right.prev = node
        node.next = self.right
        node.prev = temp
        temp.next = node


    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    
        

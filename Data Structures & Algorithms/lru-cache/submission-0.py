class Node:
    # nodes will be (key, val)
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key will be normal key, val will be a pointer to designated Node(key, val)

        self.left = Node(0,0) # nodes on the left will be LRU
        self.right = Node(0,0) # nodes on the right will be MRU

        self.left.next = self.right
        self.right.prev = self.left
    
    # helper
    def remove(self, node):
        prv = node.prev
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv

    #helper
    def insert(self, node):
        prv = self.right.prev
        prv.next = node
        node.prev = prv
        self.right.prev = node
        node.next = self.right
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key]) # removing then inserting to indicate that it is MRU and not LRU (re-arranging the node)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        

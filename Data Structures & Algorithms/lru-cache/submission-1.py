class ListNode:
    def __init__(self):
        self.val = 0
        self.prev= None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.LRUCache = {}
        self.nodeToKey= {}
        self.capacity = capacity
        self.LRU = ListNode()
        self.MRU = ListNode()
        self.length = 0
        

    def get(self, key: int) -> int:
        if key in self.LRUCache:
            node = self.LRUCache[key]
            oldNext = node.next
            oldPrev = node.prev
            oldPrev.next = oldNext
            oldNext.prev = oldPrev
            self.MRU.prev.next = node
            node.next = self.MRU
            node.prev = self.MRU.prev
            self.MRU.prev = node
            return self.LRUCache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.LRUCache:
            if not self.LRU.next:
                self.LRUCache[key] = ListNode()
                curr = self.LRUCache[key]
                self.nodeToKey[curr] = key
                curr.val = value
                self.LRU.next = curr
                curr.prev = self.LRU
                curr.next = self.MRU
                self.MRU.prev = curr
                self.length += 1
            else:
                self.LRUCache[key] = ListNode()
                self.LRUCache[key].val = value
                curr = self.LRUCache[key]
                self.nodeToKey[curr] = key
                self.MRU.prev.next = curr
                curr.prev = self.MRU.prev
                self.MRU.prev = curr
                curr.next = self.MRU
                self.length += 1
                if self.length > self.capacity:
                    remove = self.LRU.next
                    del self.LRUCache[self.nodeToKey[remove]]
                    self.length -= 1
                    remNext = remove.next
                    remNext.prev = self.LRU
                    self.LRU.next = remNext
        else:
            node = self.LRUCache[key]
            node.val = value
            oldNext = node.next
            oldPrev = node.prev
            oldPrev.next = oldNext
            oldNext.prev = oldPrev
            self.MRU.prev.next = node
            node.next = self.MRU
            node.prev = self.MRU.prev
            self.MRU.prev = node





        

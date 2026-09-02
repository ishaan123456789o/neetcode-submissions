class ListNode:
    def __init__(self):
        self.value = -1
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.back = None
        self.front = None
        self.last = None
        self.back = ListNode()
        curr = self.back
        for _ in range(k-1):
            curr.next = ListNode()
            curr = curr.next
        curr.next = self.back
        self.front = self.back
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.back.value = value
        self.last = self.back
        if self.back.next != self.front:
            self.back = self.back.next
        return True
        

        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front.value = -1
        if self.isFull():
            self.back = self.front
        self.front = self.front.next
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.value
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.last.value
        

    def isEmpty(self) -> bool:
        if self.back == self.front and self.back.value == -1:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.back.next == self.front and self.back.value != -1:
            return True
        return False

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
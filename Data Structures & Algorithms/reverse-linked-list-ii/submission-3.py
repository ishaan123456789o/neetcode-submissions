# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        curr = head
        next = curr.next
        position = 1
        while curr and position != left:
            prev = curr
            curr = curr.next
            if not curr:
                return None
            if curr.next:
                next = curr.next
            else:
                next = None
            position += 1
        leftNode = curr
        rightPrevatEnd = prev
        while position != right:
            curr.next = prev
            prev = curr
            curr = next
            if not curr:
                return None
            if curr.next:
                next = curr.next
            else:
                next = None
            position += 1
        leftNextatEnd = curr.next
        curr.next = prev
        leftNode.next = leftNextatEnd
        if not rightPrevatEnd:
            return curr
        rightPrevatEnd.next = curr
        return head

        

            
        
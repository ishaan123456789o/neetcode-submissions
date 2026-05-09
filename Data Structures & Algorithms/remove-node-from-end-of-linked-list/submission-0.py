# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        element = length - n + 1
        if element == 1:
            return head.next
        removeNode = head
        prev = head
        i = 1
        while i < element:
            removeNode = removeNode.next
            i += 1
        j = 1
        while j < element - 1:
            prev = prev.next
            j += 1
        prev.next = removeNode.next
        return head
        
        
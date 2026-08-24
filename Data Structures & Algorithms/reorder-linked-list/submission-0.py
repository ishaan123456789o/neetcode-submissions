# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(start):
            prev = None
            current = start
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        firstHalf = head
        secondHalf = head
        endFirstHalf = head
        if length % 2 == 0:
            for i in range(length//2):
                secondHalf = secondHalf.next
                if i < length//2-1:
                    endFirstHalf = endFirstHalf.next
        else:
            for i in range(length//2+1):
                secondHalf = secondHalf.next
                if i < length//2:
                    endFirstHalf = endFirstHalf.next
        endFirstHalf.next = reverse(secondHalf)
        secondHalf = endFirstHalf.next
        if length % 2 != 0:
            while secondHalf and firstHalf:
                nextFirst = firstHalf.next
                firstHalf.next = secondHalf
                secondHalf = secondHalf.next
                firstHalf = firstHalf.next
                firstHalf.next = nextFirst
                firstHalf = firstHalf.next
                endFirstHalf.next = secondHalf
        else:
            while firstHalf.next != secondHalf:
                nextFirst = firstHalf.next
                firstHalf.next = secondHalf
                secondHalf = secondHalf.next
                firstHalf = firstHalf.next
                firstHalf.next = nextFirst
                firstHalf = firstHalf.next
                endFirstHalf.next = secondHalf
            
        
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head
        res = False
        while curr:
            if curr in seen:
                res = True
                break
            seen.add(curr)
            curr = curr.next
        return res


        
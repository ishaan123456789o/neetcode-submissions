# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        res = None
        resHead = None
        while curr1 and curr2:
            if curr1.val < curr2.val:
                if not res:
                    res = curr1
                    resHead = res
                else:
                    res.next = curr1
                    res = res.next
                curr1 = curr1.next
            else:
                if not res:
                    res = curr2
                    resHead = res
                else:
                    res.next = curr2
                    res = res.next
                curr2 = curr2.next
        if curr1:
            if not res:
                res = curr1
                resHead = res
            else:
                while curr1:
                    res.next = curr1
                    res = res.next
                    curr1 = curr1.next
                res.next = None
        else:
            if not res:
                res = curr2
                resHead = res
            else:
                while curr2:
                    res.next = curr2
                    res = res.next
                    curr2 = curr2.next
                res.next = None
        return resHead
                 


        
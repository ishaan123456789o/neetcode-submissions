# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0
        resNode = ListNode()
        currRes = resNode
        while curr1 or curr2 or carry:
            if curr1 and curr2:
                if curr1.val + curr2.val + carry < 10:
                    currRes.val = curr1.val + curr2.val + carry
                    carry = 0
                    if curr1.next or curr2.next or carry:
                        currRes.next = ListNode()
                else:
                    currRes.val = (curr1.val + curr2.val + carry)%10
                    carry = (curr1.val + curr2.val + carry)//10
                    if curr1.next or curr2.next or carry:
                        currRes.next = ListNode()
                curr1 = curr1.next
                curr2 = curr2.next
            elif curr1:
                if curr1.val + carry < 10:
                    currRes.val = curr1.val + carry
                    carry = 0
                    if curr1.next or carry:
                        currRes.next = ListNode()
                else:
                    currRes.val = (curr1.val + carry)%10
                    carry = (curr1.val + carry)//10
                    if curr1.next or carry:
                        currRes.next = ListNode()
                curr1 = curr1.next
            elif curr2:
                if curr2.val + carry < 10:
                    currRes.val = curr2.val + carry
                    carry = 0
                    if curr2.next or carry:
                        currRes.next = ListNode()
                else:
                    currRes.val = (curr2.val + carry)%10
                    carry = (curr2.val + carry)//10
                    if curr2.next or carry:
                        currRes.next = ListNode()
                curr2 = curr2.next
            else:
                currRes.val = carry
                carry = 0
            if currRes.next:
                currRes = currRes.next
        currRes.next = None
        return resNode

        
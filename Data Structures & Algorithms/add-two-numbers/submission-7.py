# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 5 - 5 - 5
        # 5 - 5 - 5
        # 0 - 1 - 1 - 1
        # we need carry logic
        # l1 and l2 could be dif size 
        carry = 0
        tmp1 = l1
        tmp2 = l2
        dummy = ListNode(0)
        dummyiter = dummy
        while tmp1 or tmp2:
            # sum logic + first carry case
            if not tmp1:
                val = tmp2.val + carry
            elif not tmp2:
                val = tmp1.val + carry
            else:
                val = tmp1.val + tmp2.val + carry
            if val > 9:
                val = val - 10
                carry = 1
            else:
                carry = 0

            # linked list building
            sumNode = ListNode(val)
            dummyiter.next = sumNode

            # iteration
            if not tmp1:
                tmp2 = tmp2.next
            elif not tmp2:
                tmp1 = tmp1.next
            else:
                tmp1 = tmp1.next
                tmp2 = tmp2.next
            dummyiter = dummyiter.next
        # second carry case
        if carry == 1:
            carryNode = ListNode(1)
            dummyiter.next = carryNode
        return dummy.next

            
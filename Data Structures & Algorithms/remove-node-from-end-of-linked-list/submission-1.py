# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # runtime - O(n)
        # 0 - 1 - 2 - 3 - 4 
        # 

        dummy = ListNode(0,head)

        slow = dummy
        fast = dummy

        # make gap
        for _ in range(n+1):
            fast = fast.next
        
        # push both forward
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next
        
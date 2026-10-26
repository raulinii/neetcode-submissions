# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # iter through with fast and slow pointers
        # once we get to end, fast will be at end, slow will be at mid
        # reassign fast to head, keep slow at mid
        # reverse slow side because we pull reversed values
        # after we reverse, keep joining the heads of the two

        slow, fast = head, head.next


        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        fast = head
        
        # reverse linked list
        # 1, 2, 3, 4
        # 4, 3, 2, 1

        second = slow.next
        slow.next = prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev

    
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1,tmp2
            










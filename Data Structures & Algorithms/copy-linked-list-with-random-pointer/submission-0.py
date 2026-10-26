"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # node would be key, value with be tuple of next node and random pointer

        mydict = {}
        tmp = head
        while tmp:
            if tmp not in mydict:
                mydict[tmp] = Node(tmp.val)
            tmp = tmp.next
        mydict[None] = None
        # dict is now populated with copy: newnode with val
        # all nodes exist in memory so they can be linked now
        
        tmp = head
        while tmp:
            mydict[tmp].next = mydict[tmp.next]
            if mydict[tmp.random] == None:
                mydict[tmp].random = None
            else:
                mydict[tmp].random = mydict[tmp.random]
            tmp = tmp.next
        return mydict[head]





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            temp = current.next # point to node 2
            current.next = prev # now points to 0
            prev = current # prev is now node 1
            current = temp # now current is node 2
        
        return prev
        



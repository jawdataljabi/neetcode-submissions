# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            temp = current.next # so we have the old next before we update it
            current.next = prev
            prev = current
            current = temp
        return prev # since previous will point at the new header once current points beyond the old tail (NULL)

            
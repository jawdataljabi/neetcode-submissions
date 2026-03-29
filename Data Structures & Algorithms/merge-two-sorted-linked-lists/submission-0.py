# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = node = ListNode()

        while list1 or list2:
            if not list1 and list2:
                node.next = list2
                list2 = list2.next # MAKE SURE TO UPDATE
            elif not list2 and list1:
                node.next = list1
                list1 = list1.next
            elif list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                node.next = list2
                list2 = list2.next
            elif list1.val == list2.val:
                node.next = list1
                list1 = list1.next
                node = node.next
                node.next = list2
                list2 = list2.next
            node = node.next # this updates node, but not head since we are redefining. head still points at the true head
        return head.next
        
            

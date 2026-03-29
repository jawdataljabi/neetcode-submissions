# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 321: [1,2,3]
        # 654: [9,5,6]
        #      [0,8,9]
        # 321 + 654 = 975

        # [1,2,3]
        # [9,5]
        # [0,8,3]

        # l1 
        # l2
        dummy = ListNode()
        current = dummy
        overflow = 0

        while l1 or l2 or overflow:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            
            addition = v1 + v2 + overflow
            overflow = addition // 10 # 18 // 10 = 1
            v3 = addition % 10 # 18 % 10 = 8

            current.next = ListNode(v3)
            current = current.next

            if l1 and l1.next:
                l1 = l1.next
            else:
                l1 = None
            if l2 and l2.next:
                l2 = l2.next
            else:
                l2 = None
        
        return dummy.next

            


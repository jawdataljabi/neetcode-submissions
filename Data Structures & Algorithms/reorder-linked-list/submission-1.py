# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # idea is to use slow and fast, because when the evaluation "while fast and fast.next" stops being true,
        # then we know that slow is at the mid point of the array. From there, we can reverse the second array, and then begin
        # alternating between node1 -> node2, and node2 -> node1

        # head = [2,4,6,8,10]
        # list1 = [2,4,6]
        # list2 reversed = [10,8]

        head1 = head
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # now slow is in the middle
        head2 = slow.next
        slow.next = None

        # reverse the second linked list
        # [8,10]
        prev = None
        
        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp
        head2 = prev
        
        # head1 -> [2,4,6]
        # head2 -> [10,8]

        while head2:
            # head1: 2, head2: 10
            temp1 = head1.next # 4 | 6
            temp2 = head2.next # 8 | None

            head1.next = head2 # 2 -> 10 | 4 -> 8
            head2.next = temp1 # 10 -> 4 | 8 -> 6

            head1 = temp1 # head1: 4 | head1: 6
            head2 = temp2 # head2: 8 | head2: None
        



        

        


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # approach would be to use the slow and fast pointer method
        slow = fast = head
        
        while fast and fast.next: # what this will do is put slow in the middle meaning slow.next is
                                  # the second half of the list. we don't use fast after this, fast is 
                                  # just used to put slow in the middle
            slow = slow.next
            fast = fast.next.next

        # now we want to cut the array in half to form two, and then reverse the second array
        second = slow.next
        prev = slow.next = None # this splits (and also defines prev so that we can reverse the 2nd list)

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # now prev is the new head of the second array
        first = head
        second = prev # IF YOU DON'T PUT THIS, THEN DOING THE FOLLOWING LOOP WILL ASSUME SECOND = None
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
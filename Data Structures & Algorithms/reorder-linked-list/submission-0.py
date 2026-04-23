# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None

        prev = None

        while fast:
            temp = fast.next
            fast.next = prev
            prev = fast
            fast = temp
        fast = prev
        slow = head

        while fast:
            temp1 = fast.next
            temp2 = slow.next

            fast.next = temp2
            slow.next = fast

            slow = temp2
            fast = temp1



        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
     

        head = l1
        prev = None
        count = 0
        while l1:
            count += 1
            temp = l1.next
            l1.next = prev
            prev = l1
            l1 = temp
        head = prev
        final1 = 0
        while head:
            final1 += (10**(count - 1)) * head.val
            temp = head.next
            head = temp
       
            count -= 1

        head2 = l2
        prev2 = None
        count2 = 0
        while l2:
            count2 += 1
            temp = l2.next
            l2.next = prev2
            prev2 = l2
            l2 = temp
        
        head2 = prev2
        final2 = 0
        while head2:
            final2 += (10**(count2 - 1)) * head2.val
            temp = head2.next
            head2 = temp
            count2 -= 1
        final = final2 + final1
      
        newNode = ListNode(0)
        curr = newNode

        if final == 0:
            return ListNode(0)
        while final != 0:
            curr.next = ListNode(final % 10 )
            temp = curr.next
            curr = temp
            final = final // 10

        return newNode.next



        
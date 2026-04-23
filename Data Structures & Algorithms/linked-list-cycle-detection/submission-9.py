# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        temp = head
        head = head 
        while head:
            if head.next == None:
                return False
            temp = temp.next
            head = head.next.next
            if temp == head:
                return True


        return False
                



    
            
            


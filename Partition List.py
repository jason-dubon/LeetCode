  # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        more = ListNode()
        
        lessTail = less
        moreTail = more
        
        curr = head
        
        while curr:
            if curr.val < x:
                lessTail.next = curr
                lessTail = lessTail.next
            else:
                moreTail.next = curr
                moreTail = moreTail.next
            curr = curr.next
        
        lessTail.next = more.next 
        moreTail.next = None
        
        return less.next 
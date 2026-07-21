# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        start = end = dummy

        while left - 1 > 0: 
            start = start.next
            left -= 1
        
        while right > 0: 
            end = end.next
            right -= 1
        
        sub_start = start.next
        sub_tail_end = end.next

        cur = sub_start
        prev = sub_tail_end

        while cur != sub_tail_end: 
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        start.next = prev
        return dummy.next
        
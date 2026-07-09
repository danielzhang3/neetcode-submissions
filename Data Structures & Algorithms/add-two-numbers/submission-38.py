# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        p, q = l1, l2
        carry = 0

        while p or q or carry: 
            x = p.val if p else 0
            y = q.val if q else 0
            add = x + y + carry
            carry = add // 10
            cur.next = ListNode(add % 10)
            cur = cur.next
            p = p.next if p else None
            q = q.next if q else None
        
        return dummy.next
        
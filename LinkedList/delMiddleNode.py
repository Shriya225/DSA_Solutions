# Tortoise and hare algo...
# o(n//2)==o(n) (as consatnts r ignored..)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        fast=slow=head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        prev.next=slow.next
        return head
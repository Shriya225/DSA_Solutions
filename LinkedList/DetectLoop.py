# 141. Linked List Cycle
class Solution:
    def hasCycle(self, h):
        f=s=h
        while f and f.next:
            s=s.next
            f=f.next.next
            if f==s:
                return True
        return False
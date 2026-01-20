# 142. Linked List Cycle II
class Solution:
    def detectCycle(self, h):
        s=f=h
        while f and f.next:
            s=s.next
            f=f.next.next
            if f==s:
                s=h
                ans=-1
                while s!=f:
                    s=s.next
                    f=f.next
                return s
        return None
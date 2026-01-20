# 2 pointer soln
class Solution:
    def middleNode(self, h):
        f=s=h
        while f and f.next:
            s=s.next
            f=f.next.next
        return s
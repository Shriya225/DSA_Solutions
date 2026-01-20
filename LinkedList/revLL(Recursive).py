# 206. Reverse Linked List
class Solution:
    def reverseList(self, h):
        def helper(p,c):
            if not c:
                return p
            y=c.next
            c.next=p
            return helper(c,y)
        return helper(None,h)
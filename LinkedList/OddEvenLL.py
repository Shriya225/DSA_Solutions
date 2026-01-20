
class Solution:
    def oddEvenList(self, h):
        if not h:
            return 
        e_h=e=None
        o_h=o=None
        x=h
        c=1
        while x:
            y=x.next
            x.next=None
            if c%2==0:
                if e_h:
                    e.next=x
                    e=x
                else:
                    e_h=e=x
            else:
                if o_h:
                    o.next=x
                    o=x
                else:
                    o_h=o=x
            c+=1
            x=y
        o.next=e_h
        return o_h
class Node:
    def __init__(self,v):
        self.data=v
        self.next=None

class LL:
    def __init__(self):
        self.h=None
    def insert_beg(self,d):
        if not self.h:
            self.h=Node(d)
        else:
            n=Node(d)
            n.next=self.h
            self.h=n
    def insert_end(self,d):
        if not self.h:
            self.h=Node(d)
        else:
            x=self.h
            while x.next:
                x=x.next
            x.next=Node(d)
    def insert_after(self,ele,d):
        n=Node(d)
        x=self.h
        while x:
            if x.data==ele:
                y=x.next
                x.next=n
                n.next=y
                break
            x=x.next
    def insert_before(self,ele,d):
        n=Node(d)
        x=self.h
        prev=None
        while x:
            if x.data==ele:
                if prev:
                    prev.next=n
                    n.next=x
                else:
                    n.next=x
                    self.h=n
                break
            prev=x
            x=x.next
    def delNode(self,ele):
        x=self.h
        prev=None
        while x:
            if x.data==ele:
                if prev:
                    prev.next=x.next
                else:
                    self.h=self.h.next
                break
            prev=x
            x=x.next
    def length(self):
        x=self.h
        ans=0
        while x:
            ans+=1
            x=x.next
        return ans
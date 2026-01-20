class Node:
    def __init__(self,v):
        self.data=v
        self.next=None
        self.prev=None
    
class DLL:
    def __init__(self):
        self.h=None
    def insert_beg(self,d):
        n=Node(d)
        if not self.h:
            self.h=n
        else:
            n.next=self.h
            self.h=n


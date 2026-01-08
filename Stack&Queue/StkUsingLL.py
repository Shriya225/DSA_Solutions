class Node:
    def __init__(self,d):
        self.data=d
        self.next=None
class LL:
    def __init__(self):
        self.h=None
    def push(self,ele):
        if not self.h:
            self.h=Node(ele)
        else:
            n=Node(ele)
            n.next=self.h
            self.h=n
    def pop(self):
        if not self.h:
            print("stk underflow")
            return None
        val=self.h.data
        self.h=self.h.next
        return val
l1=LL()
l1.push(5)
l1.push(6)
l1.pop()
l1.pop()
l1.pop()



    
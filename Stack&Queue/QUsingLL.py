# Q usign LL
class Node:
    def __init__(self,d):
        self.data=d
        self.next=None
class LL:
    def __init__(self):
        self.f=None
        self.r=None
    def enQ(self,ele):
        if not self.f:
            self.f=self.r=Node(ele)
        else:
            n=Node(ele)
            self.r.next=n
            self.r=n
    def deQ(self):
        if self.f==None:
            print("Q is empty")
            return None
        val=self.f
        self.f=self.f.next
        return 





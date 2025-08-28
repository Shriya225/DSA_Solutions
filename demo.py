class Node:
    def __init__(self,d,n=None):
        self.data=d
        self.next=n
class LL:
    def __init__(self):
        self.head=None
    def insertbeg(self,d):
        n=Node(d)
        if not self.head:
            self.head=n
        else:
            n.next=self.head
            self.head=n
    def printLL(self):
        if not self.head:
            print("LL is Empty...")
        else:
            p=self.head
            while p:
                print(p.data," --> ",end=" ")
                p=p.next
    def middleEle(self):
        if not self.head:
            print("LL is empty..")
        s=f=self.head
        while f and f.next:
            s=s.next
            f=f.next.next
        print("Middle elemtent is :",s.data)

ll=LL()
ll.insertbeg(1)
ll.insertbeg(2)
ll.insertbeg(3)
ll.insertbeg(4)
ll.insertbeg(5)
ll.printLL()
ll.middleEle()


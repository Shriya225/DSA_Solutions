# Linked list..
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertBeginning(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            n=Node(data)
            n.next=self.head
            self.head=n
    def insertAfter(self,data,ele):
        h=self.head
        while h!=None:
            if h.data==ele:
                n=Node(data)
                n.next=h.next
                h.next=n
                return
            h=h.next
        print("Sorry there is no such data")
    def deleteNode(self,data):
        prev=None
        if self.head==None:
            print("LL is empty...")
        else:
            h=self.head
            while h!=None:
                if h.data==data:
                    if prev!=None:
                        prev.next=h.next
                    else:
                        self.head=self.head.next
                prev=h
                h=h.next
            print()
    def display(self):
        if self.head==None:
            print("LL is empty...")
        else:
            h=self.head
            while h!=None:
                print(h.data,"-->  ",end=" ")
                h=h.next
            print()


ll=LinkedList()
ll.display()
ll.insertBeginning(1)
ll.display()
ll.insertBeginning(2)
ll.display()
ll.insertBeginning(3)
ll.display()
ll.insertAfter(22,22)
ll.display()
ll.insertAfter(16,2)
ll.display()
ll.deleteNode(3)
ll.display()
ll.deleteNode(16)
ll.display()
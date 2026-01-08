class Queue:
    def __init__(self,size):
        self.f=self.r=-1
        self.size=size
        self.a=[None]*size
    def enQueue(self,ele):
        if self.r==self.size-1:
            print("Queu is full")
            return
        if self.f==-1:
            self.f+=1
        self.r+=1
        self.a[self.r]=ele
    def deQueue(self):
        if self.f==-1:
            print("Queue is empty")
            return 
        val=self.a[self.f]
        self.f+=1





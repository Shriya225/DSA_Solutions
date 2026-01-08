# circualr Q
class CircularQ:
    def __init__(self,s):
        self.s=s
        self.c=0
        self.f=0
        self.r=-1
        self.a=[None]*s
    def enqueue(self,ele):
        if self.c==self.s:
            print("Queue is full")
            return 
        self.r=(self.r+1)%self.s
        self.c+=1
        self.a[self.r]=ele
    def deQueue(self):
        if self.c==0:
            print("Queue is empty")
            return None
        val=self.a[self.f]
        self.a[self.f]=None
        self.c-=1
        self.f=(self.f+1)%self.s
        return val



# 1 based index heap
class Maxheap:
    def __init__(self):
        self.h=[-100]
    def insert(self,x):
        if not self.h:
            self.h.append(x)
            return
        self.h.append(x)
        i=len(self.h)-1
        while i>1:
            p=i//2
            if self.h[p]<self.h[i]:
                self.h[p],self.h[i]=self.h[i],self.h[p]
                i=p
            else:
                break
    def deletion(self):
        if len(self.h)==1:
            return None
        if len(self.h)==2:
            return self.h.pop()
        r=self.h[1]
        y=self.h.pop()
        self.h[1]=y
        n=len(self.h)-1
        i=1
        while True:
            l=2*i
            r=2*i+1
            m=i
            if l<=n and self.h[l]>self.h[m]:
                m=l
            if r<=n and self.h[r]>self.h[m]:
                m=r
            if m!=i:
                self.h[m],self.h[i]=self.h[i],self.h[m]
                i=m
            else:
                break
        return r
            
        






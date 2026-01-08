# pop takes O(n)
# rest O(1)
# SC-O(n)

# dynamic Q
class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,ele):
        self.queue.append(ele)
    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop(0)
    def peek(self):
        if not self.queue:
            return None
        return self.queue[0]

q1=Queue()
q1.enqueue(1)
print(q1.peek())
q1.enqueue(2)
print(q1.peek())



# standadrd Q
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
        return val


    

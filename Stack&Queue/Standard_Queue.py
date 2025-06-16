# pop takes O(n)
# rest O(1)
# SC-O(n)
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

    

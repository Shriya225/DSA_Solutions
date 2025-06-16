# STk using 2 queues!!!!
class MyStack:

    def __init__(self):
        self.q1=[]
        self.q2=[]

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if not self.q1:
            return None
        while len(self.q1)>1:
            self.q2.append(self.q1.pop(0))
        x=self.q1.pop(0)
        self.q1,self.q2=self.q2,self.q1
        return x

    def top(self) -> int:
        if not self.q1:
            return 
        while len(self.q1)>1:
            self.q2.append(self.q1.pop(0))
        x=self.q1[0]
        self.q2.append(self.q1.pop(0))
        self.q1,self.q2=self.q2,self.q1
        return x
        

    def empty(self) -> bool:
        if not self.q1:
            return True
        return False
        
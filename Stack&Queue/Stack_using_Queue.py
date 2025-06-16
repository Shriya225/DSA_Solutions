# using 1 queue
class MyStack:

    def __init__(self):
        self.q1=[]

    def push(self, x: int) -> None:
        l=len(self.q1)
        self.q1.append(x)
        for i in range(l):
            self.q1.append(self.q1.pop(0))

    def pop(self) -> int:
        if not self.q1:
            return None
        return self.q1.pop(0)
        

    def top(self) -> int:
        if not self.q1:
            return None
        return self.q1[0]
        

    def empty(self) -> bool:
        if not self.q1:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
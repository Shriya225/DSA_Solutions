# Stack

# implementing using Array

# TC-O(1)
# SC-O(n)

class Stack:
    def __init__(self):
        self.stk=[]
    def push(self,ele):
        self.stk.append(ele)
    def pop(self):
        if not self.stk:
            return None
        return self.stk.pop(-1)
    def peek(self):
        if not self.stk:
            return None
        return self.stk[-1]

stk1=Stack()
stk1.push(2)
print(stk1.peek())
print(stk1.pop())
print(stk1.peek())
stk1.push(3)
stk1.push(33)
stk1.push(1)
print(stk1.peek())

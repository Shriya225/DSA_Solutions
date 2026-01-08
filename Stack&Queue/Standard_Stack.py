# Stack

# implementing using Array
#  dynmaic stk implemetntion

# TC-O(1)
# SC-O(n)

# class Stack:
#     def __init__(self):
#         self.stk=[]
#     def push(self,ele):
#         self.stk.append(ele)
#     def pop(self):
#         if not self.stk:
#             return None
#         return self.stk.pop(-1)
#     def peek(self):
#         if not self.stk:
#             return None
#         return self.stk[-1]

# stk1=Stack()
# stk1.push(2)
# print(stk1.peek())
# print(stk1.pop())
# print(stk1.peek())
# stk1.push(3)
# stk1.push(33)
# stk1.push(1)
# print(stk1.peek())




# fixed size arr method
# size limit
# overflow and underlow conditions

class Stkac2:
    def __init__(self,size):
        self.a=[None]*size
        self.size=size
        self.top=-1
    def push(self,ele):
        if self.top==self.size-1:
            print(self.a,self.top)
            print("stack overflow.")
            return
        print(self.a,self.top)
        self.top+=1
        self.a[self.top]=ele
    def pop(self):
        if self.top==-1:
            print("stack underflow.")
            return None
        val=self.a[self.top]
        self.a[self.top]=None
        self.top-=1
        return val

    def peek(self):
        if self.top==-1:
            print("stk is empty")
            return None
        return self.a[self.top]
s=Stkac2(3)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()



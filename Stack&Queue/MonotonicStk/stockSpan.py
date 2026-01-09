# just prev greter ele distance

def stockSpan(a):
    stk=[]
    ans=[1]*len(a)
    for i in range(len(a)):
        while stk and a[stk[-1]]<=a[i]:
            stk.pop()
        if stk and a[stk[-1]]>a[i]:
            ans[i]=i-stk[-1]
        # very imprtant edge case 
        if not stk:
            ans[i]=i+1
        stk.append(i)
    return ans
        

a=list(map(int,input("A:").split()))
print(stockSpan(a))




# 901. Online Stock Span
class StockSpanner:

    def __init__(self):
        self.a=[]
        self.stk=[]

    def next(self,x: int) -> int:
        self.a.append(x)
        while self.stk and self.a[self.stk[-1]]<=x:
            self.stk.pop()
        if not self.stk:
            self.stk.append(len(self.a)-1)
            return len(self.a)
        if self.stk and self.a[self.stk[-1]]>x:
            ans=len(self.a)-1-self.stk[-1]
            self.stk.append(len(self.a)-1)
            return ans
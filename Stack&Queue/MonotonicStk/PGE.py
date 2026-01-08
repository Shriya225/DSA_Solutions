
def pge(a,b):
    ans=[]
    stk=[]
    d=dict()
    for i in b:
        while stk and i>stk[-1]:
            stk.pop()
        if not stk:
            d[i]=-1
        else:
            d[i]=stk[-1]
        stk.append(i)
    return d

a=list(map(int,input("A:").split()))
b=list(map(int,input("b:").split()))
print(pge(a,b))
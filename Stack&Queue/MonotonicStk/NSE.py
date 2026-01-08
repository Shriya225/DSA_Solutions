
def nse(a,b):
    ans=[]
    stk=[]
    d=dict()
    for i in b:
        while stk and i<stk[-1]:
            d[stk.pop()]=i
        stk.append(i)
    while stk:
        d[stk.pop()]=-1

    for i in a:
        ans.append(d[i])
    return ans
a=list(map(int,input("A:").split()))
b=list(map(int,input("b:").split()))
print(nse(a,b))
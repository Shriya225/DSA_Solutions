# Binary search(lower bound)
def bs2(a,t):
    l,h=0,len(a)-1
    while l<=h:
        m=(l+h)//2
        if a[m]==t:
            return m
        elif a[m]>t:
            h=m-1
        else:
            l=m+1
    return l

def Lis_bs(a):
    ans=[]
    for i in range(len(a)):
        if not ans or  a[i]>ans[-1]:
            ans.append(a[i])
        else:
            x=bs2(ans,a[i])
            ans[x]=a[i]
    return len(ans)

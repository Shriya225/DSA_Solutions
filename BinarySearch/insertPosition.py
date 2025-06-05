# 35. Search Insert Position
# lower bound problem
def insertpos(a,t):
    if a[0]>t:
        return 0
    if a[-1]<t:
        return len(a)
    l,h=0,len(a)-1
    ans=-1
    while l<=h:
        m=(l+h)//2
        if a[m]==t:
            return m
        elif a[m]>t:
            ans=m
            h=m-1
        else:
            l=m+1
    return ans
a=list(map(int,input("a:").split()))
t=int(input("T:"))
insertpos(a,t)  
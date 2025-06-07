# 2064. Minimized Maximum of Products Distributed to Any Store
import math
def helper(a,mid):
    s=0
    for i in a:
        s+=math.ceil(i/mid)
    return s
def minMaximized(a,stores):
    l,h=1,max(a)
    ans=-1
    while l<=h:
        m=(l+h)//2
        x=helper(a,m)
        if x<=stores:
            ans=m
            h=m-1
        else:
            l=m+1
    return ans
a=list(map(int,input("a:").split()))
q=int(input("stores:"))
print(minMaximized(a,q))
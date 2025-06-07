import math
def helper(a,mid):
    c=0
    for i in a:
        if i>mid:
            c+=(i-1)//mid
    return c
def minLimit(a,k):
    l,h=1,max(a)
    ans=-1
    while l<=h:
        m=(l+h)//2
        x=helper(a,m)
        print("m:",m,"x:",x)
        if x<=k:
            ans=m
            h=m-1
        else:
            l=m+1
    return ans
a=list(map(int,input("a:").split()))
k=int(input("K:"))
print(minLimit(a,k))
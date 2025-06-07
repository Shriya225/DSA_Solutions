# 1283. Find the Smallest Divisor Given a Threshold
import math
def helper(a,m):
    s=0
    for i in a:
        s+=math.ceil(i/m)
    return s
def smallDivisor(a,t):
    l,h=1,max(a)
    ans=-1
    while l<=h:
        m=(l+h)//2
        x=helper(a,m)
        if x<=t:
            ans=m
            h=m-1
        else:
            l=m+1
    return ans
a=list(map(int,input("a:").split()))
t=int(input("T:"))
print(smallDivisor(a,t))  
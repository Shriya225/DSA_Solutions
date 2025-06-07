# 1011. Capacity To Ship Packages Within D Days
def helper(a,m):
        c=0
        s=0
        for i in range(len(a)):
            s+=a[i]
            if s==m:
                s=0
                c+=1
            elif s>m:
                s=a[i]
                c+=1
            if i==len(a)-1:
                if s<m and s!=0:
                    c+=1
            if a[i]>m:
                break
        return c
    

def CapacityToShip(a,t):
    l,h=max(a),sum(a)
    if t==1:
        return h
    print(l+h)
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
print(CapacityToShip(a,t)) 
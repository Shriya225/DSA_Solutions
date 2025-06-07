# 2226. Maximum Candies Allocated to K Children

def helper(a,mid):
    s=0
    for i in a:
        s+=i//mid
    return s
def Candies(a,k):
    if sum(a)<k:
        return 0
    l,h=1,max(a)
    ans=-1
    while l<=h:
        m=(l+h)//2
        x=helper(a,m)
        print("x:",x,"m",m)
        if x>=k:
            ans=m
            l=m+1
        else:
            h=m-1
    return ans
a=list(map(int,input("a:").split()))
q=int(input("stores:"))
print(Candies(a,q))

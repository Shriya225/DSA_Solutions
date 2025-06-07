# 1482. Minimum Number of Days to Make m Bouquets

# O(n*log(max(a)-min(a)))

def helper(a,mid,k):
    totalBoquets=0
    c=0
    for i in a:
        if i<=mid:
            c+=1
            if c==k:
                c=0
                totalBoquets+=1
        else:
            c=0
    return totalBoquets
def makeBoquet(a,b,k):
    if k*b>len(a):
        return -1
    ans=-1
    l,h=min(a),max(a)
    while l<=h:
        m=(l+h)//2
        x=helper(a,m,k)
        if x<=b:
            ans=m
            h=m-1
        else:
            l=m+1
    return ans

a=list(map(int,input("a:").split()))
h=int(input("b:"))
k=int(input("k:"))
print(makeBoquet(a,h,k))  
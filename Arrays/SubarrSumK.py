# 560. Subarray Sum Equals K
# prefix sum
# o(n)
def subarraySum(a,k,n):
    d={}
    s=c=0
    for i in range(n):
        s+=a[i]
        if s==k:
            c+=1
        if s-k in d:
            c+=d[s-k]
        d[s]=d.get(s,0)+1
    print("c:",c)

a=list(map(int,input("a:").split()))
k=int(input("K:"))
subarraySum(a,k,len(a))
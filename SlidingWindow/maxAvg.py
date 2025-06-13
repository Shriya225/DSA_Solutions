# Classic fixed size window problem..

#  [1,2,1,23,4,5,6,7]

def maxAvg(a,k):
    l=0
    ans=float('-inf')
    s=0
    for i in range(k):
        s+=a[i]
    ans=max(ans,s)
    for r in range(k,len(a)):
        s-=a[l]
        l+=1
        s+=a[r]
        ans=max(ans,s)
    return ans/k
        


a=list(map(int,input("a:").split()))
k=int(input("K:"))
print(maxAvg(a,k))
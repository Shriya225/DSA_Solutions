# prefix sum
# o(n)
# sc-o(n)
def longestSubarr2(a,k):
    d={}
    s=0
    maxlen=0
    for i in range(len(a)):
        s+=a[i]
        if s==k:
            maxlen=max(maxlen,i+1)
            print("len is ",maxlen)
        if s-k in d:
            maxlen=max(i-d[s-k],maxlen)
        d[s]=min(d.get(s,float('inf')),i)
    print("maxlen",maxlen)

l=list(map(int,input("a:").split()))
k=int(input("K:"))
longestSubarr2(l,k)
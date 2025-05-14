def LongestSubArr3(a,k):
    l=s=maxlen=0
    for h in range(len(a)):
        s+=a[h]
        while s>k:
            s-=a[l]
            l+=1
        if s==k:
            maxlen=max(maxlen,h-l+1)
    return maxlen
 
l=list(map(int,input("a:").split()))
k=int(input("K:"))
LongestSubArr3(l,k)
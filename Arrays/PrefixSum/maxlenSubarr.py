# 525. Contiguous Array
def maxlenSubarr(a):
    d=dict()
    s=0
    ans=0
    for i in range(len(a)):
        if a[i]==0:
           s+=-1
        else:
           s+=1
        if s==0:
           ans=max(ans,i+1)
        if s in d:
           ans=max(ans,i-d[s])
        else:
           d[s]=i
    return ans
a=list(map(int,input("a:").split()))
print(maxlenSubarr(a))
        
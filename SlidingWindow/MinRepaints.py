# 2379. Minimum Recolors to Get K Consecutive Black Blocks

def minPaints(a,k):
    l=0
    ans=float('inf')
    c=0
    for r in range(len(a)):
        if a[r]=='W':
            c+=1
        while r-l+1>k:
            if a[l]=='W':
                c-=1
            l+=1
        if r-l+1==k:
            ans=min(ans,c)
    return ans


a=input("a:")
k=int(input("K:"))
print(minPaints(a,k))
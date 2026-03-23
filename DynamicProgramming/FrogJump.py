
def frogJump(arr,n,s=0,a=0):
    if s==n-1:
        return a
    if n==s:
        return -1
    l=frogJump(arr,n,s+1,abs(arr[s]-arr[s+1]))
    r=frogJump(arr,n,s+2,abs(arr[s]-arr[s+2]))
    if l!=-1 and r!=-1:
        return min(l,r)
    if l==-1:
        return r
    return l


# def frogJump(arr,n,s=0,a=0):
#     if s==n-1:
#         return a
#     if n==s:
#         return -1
#     l=frogJump(arr,n,s+1,abs(arr[s]-arr[s+1]))
#     r=frogJump(arr,n,s+2,abs(arr[s]-arr[s+2]))
#     if l!=-1 and r!=-1:
#         return min(l,r)
#     if l==-1:
#         return r
#     return l

# def fj(a,n,i=0,ans=0):
#     l=r=float("inf")
#     if i+1<n:
#         l=fj(a,n,i+1,ans+abs(a[i]-a[i+1]))
#     if i+2<n:
#         r=fj(a,n,i+2,ans+abs(a[i]-a[i+2]))
#     return min(l,r)


# striver dp recursion reln
def fjump(a,i):
    if i<=0:
        return 0
    l=fjump(a,i-1)+abs(a[i]-a[i-1])
    r=float('inf')
    if i>1:
        r=fjump(a,i-2)+abs(a[i]-a[i-2])
    return min(l,r)

a=list(map(int,input().split()))
n=len(a)
dp=[-1]*n


# striver dp memoization...
def fjump(a,i,dp):
    if i<=0:
        return 0
    if dp[i]!=-1:
        return dp[i]
    l=fjump(a,i-1)+abs(a[i]-a[i-1],dp)
    r=float('inf')
    if i>1:
        r=fjump(a,i-2)+abs(a[i]-a[i-2],dp)
    dp[i]=min(l,r)
    return min(l,r)

a=list(map(int,input().split()))
n=len(a)


# tabulation O(n)
def fj2(a):
    dp=[-1]*len(a)
    dp[0]=0
    for i in range(1,n):
        l=dp[i-1]+abs(a[i]-a[i-1])
        r=float("inf")
        if i>1:
            r=dp[i-2]+abs(a[i]-a[i-2])
        dp[i]=min(l,r)
    return dp[len(a)-1]

# tabulation O(1) space optimized
def fj2(a):
    n=len(a)
    x=0
    y=0
    for i in range(1,n):
        l=x+abs(a[i]-a[i-1])
        r=float("inf")
        if i>1:
            r=y+abs(a[i]-a[i-2])
        ans=min(l,r)
        y=x
        x=ans
    return x


# ...............
# forward version of dp
# from 0 to n
def fjForward(a,i,dp):
    if i==len(a)-1:
        return 0
    l=abs(a[i]-a[i+1])+fjForward(a,i+1,dp)
    r=float("inf")
    if i<len(a)-2:
        r=abs(a[i]-a[i+2])+fjForward(a,i+2,dp)
    return min(l,r)
        



# GFG
# Rod Cutting

# reccurence rel'n
def rc(a,i,t):
    if t==0:
        return 0
    if i<0:
        return float("-inf")
    r=float('-inf')
    l=rc(a,i-1,t)
    if t-(i+1)>=0:
        r=rc(a,i,t-(i+1))+a[i]
    return max(l,r)

# memoization
def rc_memo(a,i,t,dp):
    if t==0:
        return 0
    if i<0:
        return float("-inf")
    if dp[i][t]!=-1:return dp[i][t]
    r=float('-inf')
    l=rc_memo(a,i-1,t,dp)
    if t-(i+1)>=0:
        r=rc_memo(a,i,t-(i+1),dp)+a[i]
    dp[i][t]=max(l,r)
    return max(l,r)

# tabualte
def rc_memo(a):
    n=len(a)
    dp=[[0]*(n+1) for i in range(n)]
    # base case
    dp[0][0]=0
    for j in range(n+1):
        dp[0][j] = j * a[0]
    # fill dp
    for i in range(1,n):
        for j in range(n+1):
            r=float('-inf')
            l=dp[i-1][j]
            if j-(i+1)>=0:
                r=dp[i][j-(i+1)]+a[i]
            dp[i][j]=max(l,r)
    return dp[-1][-1]

# space optimize this..
# 1D optimization...
# most optimal
def rc_memo(a):
    n=len(a)
    dp=[0]*(n+1)
    # base case
    for j in range(n+1):
        dp[j] = j * a[0]
    # fill dp
    for i in range(1,n):
        for j in range(n+1):
            r=float('-inf')
            l=dp[j]
            if j-(i+1)>=0:
                r=dp[j-(i+1)]+a[i]
            dp[j]=max(l,r)
    return dp[-1]



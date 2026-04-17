# 64. Minimum Path Sum

# reccurence reln
def minpath(a,i,j):
    if i==0 and j==0:
        return a[0][0]
    elif i<0 or j<0:
        return float('inf')
    x=a[i][j]
    l=minpath(a,i-1,j)
    u=minpath(a,i,j-1)
    return x+min(l,u)

# memoization
def minpath(a,i,j,dp):
    if i==0 and j==0:
        return a[0][0]
    elif i<0 or j<0:
        return float('inf')
    if dp[i][j]!=-1:return dp[i][j]
    x=a[i][j]
    l=minpath(a,i-1,j,dp)
    u=minpath(a,i,j-1,dp)
    dp[i][j]=x+min(l,u)
    return dp[i][j]


# Tabulation
def minsum_tab(a):
    dp=[[-1]*len(a[0]) for _ in range(len(a))]
    dp[0][0]=a[0][0]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i==0 and j==0:continue
            l=r=float("inf")
            if j-1>=0:
                l=dp[i][j-1]
            if i-1>=0:
                r=dp[i-1][j]
            dp[i][j]=a[i][j]+min(l,r)
    return dp[-1][-1]

       
# space opt..
def minsum_tab(a):
    dp=[0]*len(a[0])
    for i in range(len(a)):
        x=[-1]*len(a[0])
        for j in range(len(a[0])):
            if i==0 and j==0:
                x[0]=a[0][0]
                continue
            l=r=float("inf")
            if j-1>=0:
                l=x[j-1]
            if i-1>=0:
                r=dp[j]
            x[j]=a[i][j]+min(l,r)
        dp=x
    return dp[-1]
                

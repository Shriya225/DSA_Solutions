# 120. Triangle
# reccurence rel'n
def triangele(a,i,j):
    if i==len(a)-1:
        return a[i][j]
    x=a[i][j]
    l=triangele(a,i+1,j)
    r=triangele(a,i+1,j+1)
    return x+min(l,r)

# memoization...
# got TLE in Leetcode.
def triangele(a,i,j,dp):
    if i==len(a)-1:
        return a[i][j]
    if dp[i][j]!=-1:return dp[i][j]
    x=a[i][j]
    l=triangele(a,i+1,j,dp)
    r=triangele(a,i+1,j+1,dp)
    dp[i][j]=x+min(l,r)
    return dp[i][j]

# tabulation...
def tri_tab(a):
    dp=[[0]*i for i in range(len(a[-1]))]
    print(dp)
    for i in range(len(a[-1])):
        dp[-1][i]=a[-1][i]
    print(dp)
    for r in range(len(a)-2,-1,-1):
        for c in range(r+1):
            dp[r][c]=min(a[r][c]+dp[r+1][c],a[r][c]+dp[r+1][c+1])
    return dp[0][0]

# space optimized...
# 2 arrays
def tri_tab(a):
    dp=[0]*(len(a[-1]))
    for i in range(len(a[-1])):
        dp[i]=a[-1][i]
    for r in range(len(a)-2,-1,-1):
        x=[0]*(len(a[-1]))
        for c in range(r+1):
            x[c]=min(a[r][c]+dp[c],a[r][c]+dp[c+1])
        dp=x
    return dp[0]


# space optimized...
# Most optiaml way...
# O(n)-sc
# O(n^2)-tc
def tri_tab(a):
    dp=[0]*(len(a[-1]))
    for i in range(len(a[-1])):
        dp[i]=a[-1][i]
    for r in range(len(a)-2,-1,-1):
        for c in range(r+1):
            dp[c]=min(a[r][c]+dp[c],a[r][c]+dp[c+1])
    return dp[0]



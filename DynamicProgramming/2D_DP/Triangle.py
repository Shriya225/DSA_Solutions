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

# tabulation..

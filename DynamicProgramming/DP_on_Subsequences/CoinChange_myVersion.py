# 322. Coin Change

# reccurence rel'n
# this gets TLE but my approach..
def coinChange(a,t,i):
    if t==0 :
        return 0
    if i<0:
         return float("inf")
    ans=float("inf")
    for j in range(t//a[i]+1):
            ans=min(ans,coinChange(a,t-(a[i]*j),i-1)+j)
    return ans


# memoization..

# this gets TLE but my approach..

def coinChange_memo(a,t,i,dp):
    if t==0 :
        return 0
    if i<0:
         return float("inf")
    if dp[i][t]!=-1:return dp[i][t]
    ans=float("inf")
    for j in range(t//a[i]+1):
            ans=min(ans,coinChange_memo(a,t-(a[i]*j),i-1)+j)
    dp[i][t]=ans
    return ans


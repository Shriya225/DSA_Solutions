
# reccurence rel'n
def cchange(a,t,i):
    if t==0:
        return 0
    if i<0:
        return float('inf')
    l=float('inf')
    r=cchange(a,t,i-1)
    if a[i]<=t:
        l=1+cchange(a,t-a[i],i)
    return min(l,r)


# memoization..
class Solution:
    def coinChange(self, a, t: int) -> int:
        def cchange(a,t,i,dp):
            if t==0:
                return 0
            if i<0:
                return float('inf')
            if dp[i][t]!=-1:return dp[i][t]
            l=float('inf')
            r=cchange(a,t,i-1,dp)
            if a[i]<=t:
                l=1+cchange(a,t-a[i],i,dp)
            dp[i][t]=min(l,r)
            return min(l,r)
        dp=[[-1]*(t+1) for i in range(len(a))]
        x=cchange(a,t,len(a)-1,dp)
        return x if x!=float('inf') else -1
    
# tabulation
def cchange_tab(a,t):
    dp=[[float("inf")]*(t+1) for i in range(len(a))]

        
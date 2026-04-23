# 322. Coin Change

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
    # base case
    for i in range(len(a)):
        dp[i][0] = 0
    for i in range(a[0],t+1):
        if i%a[0]==0:
            dp[0][i]=i//a[0]
    # fill dp
    for i in range(1,len(a)):
        for j in range(t+1):
            l=float('inf')
            r=dp[i-1][j]
            if a[i]<=j:
                l=1+dp[i][j-a[i]]
            dp[i][j]=min(l,r)
    return dp[-1][-1]

# space optimized code.....

def cchange_tab(a,t):
    dp=[float("inf")]*(t+1) 
    # base case
    dp[0] = 0
    for i in range(a[0],t+1):
        if i%a[0]==0:
            dp[i]=i//a[0]
    # fill dp
    for i in range(1,len(a)):
        x=[float("inf")]*(t+1) 
        for j in range(t+1):
            l=float('inf')
            r=dp[j]
            if a[i]<=j:
                l=1+x[j-a[i]]
            x[j]=min(l,r)
        dp=x
    return dp[-1]


# space optimized without using temp array....
# most optimal osln
class Solution:
    def coinChange(self, a, t: int) -> int:
        dp=[float("inf")]*(t+1) 
        # base case
        dp[0] = 0
        for i in range(a[0],t+1):
            if i%a[0]==0:
                dp[i]=i//a[0]
        # fill dp
        for i in range(1,len(a)):
            for j in range(t+1):
                l=float('inf')
                r=dp[j]
                if a[i]<=j:
                    l=1+dp[j-a[i]]
                dp[j]=min(l,r)
        return dp[-1] if dp[-1]!=float('inf') else -1

        
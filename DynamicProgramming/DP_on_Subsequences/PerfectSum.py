# Perfect Sum Problem (GFG)

# reccurenec rel'n
def psum(a,i,t):
    if t==0:
        return 1
    if i==0:
        return 1 if a[i]==t else 0
    l=psum(a,i-1,t-a[i])
    r=psum(a,i-1,t)
    return l+r


# memoization
def psum(a,i,t,dp):
    # spl case
    if i == 0:
                if t == 0 and a[0] == 0:
                    return 2
                if t == 0:
                    return 1
                if t == a[0]:
                    return 1
                return 0
    if dp[i][t]!=-1:return dp[i][t]
    if t-a[i]>=0:
        l=psum(a,i-1,t-a[i],dp)
    r=psum(a,i-1,t,dp)
    dp[i][t]=l+r
    return dp[i][t]


class Solution:
    def perfectSum(self, a, t):
        def psum(a,i,t,dp):
            if t==0:
                return 1 if a[i]!=0 else 2
            if i==0:
                return 1 if a[i]==t else 0
            if dp[i][t]!=-1:return dp[i][t]
            l=0
            if t-a[i]>=0:
                l=psum(a,i-1,t-a[i],dp)
            r=psum(a,i-1,t,dp)
            dp[i][t]=l+r
            return dp[i][t]
        dp=[[-1]*(t+1) for i in range(len(a))]
        return psum(a,len(a)-1,t,dp)
        # code here


# tabualtion..

# tabualtion..
def subseq_tab(a,k):
    dp=[[0]*(k+1) for _ in range(len(a))]
    # base case
    for i in range(k+1):
        if i==0:
            dp[0][0]=2
        else:
            dp[0][i]=1 if a[0]==i else False
    # tabulate..
    for i in range(1,len(a)):
        for j in range(k+1):
            if j==0:
                dp[i][0]=1
            else:
                l=r=0
                l=dp[i-1][j]
                if j-a[i]>=0:
                    r=dp[i-1][j-a[i]]
                dp[i][j]=l+r
    return dp[len(a)-1][k]



# 62. Unique Paths
# reccurence reln
ans=0
def uq(m,n,i,j):
    global ans
    if i==m-1 and j==n-1:
        ans+=1
        return
    if j+1<n:
        uq(m,n,i,j+1)
    if i+1<m:
        uq(m,n,i+1,j)


# clean way to write reccurenec rel'n
def uq(m,n,i,j):
    if i==m-1 and j==n-1:
        return 1
    ways=0
    if j+1<n:
        ways+=uq(m,n,i,j+1)
    if i+1<m:
        ways+=uq(m,n,i+1,j)
    return ways

# memoization...
# o to end

def uq_memo(m,n,i,j,dp):
    if i==m-1 and j==n-1:
        return 1
    if dp[i][j]!=-1:return dp[i][j]
    ans=0
    if j+1<n:
        ans+=uq_memo(m,n,i,j+1,dp)
    if i+1<m:
        ans+=uq_memo(m,n,i+1,j,dp)
    dp[i][j]=ans
    return ans

# memoization
# end to 0 (top- down) lol
def uq_memo2(m,n,i,j,dp):
    if i==0 and j==0:
        return 1
    if i<0 or j<0:
        return 0
    if dp[i][j]!=-1:return dp[i][j]
    l=uq_memo2(m,n,i-1,j,dp)
    u=uq_memo2(m,n,i,j-1,dp)
    dp[i][j]=l+u
    return dp[i][j]


# tabualtion
def uq_tab(m,n):
    dp=[[-1]*n for _ in range(m)]
    dp[0][0]=1
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:continue
            l=u=0
            if i-1>=0:
                l=dp[i-1][j]
            if j-1>=0:
                u=dp[i][j-1]
            dp[i][j]=l+u
    return dp[m-1][n-1]


# space optimization
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def uq_tab(m,n):
            dp=[-1]*n
            dp[0]=1
            for i in range(m):
                x=[-1]*n
                for j in range(n):
                    if i==0 and j==0:
                        x[0]=1
                        continue
                    l=u=0
                    if j-1>=0:
                        l=x[j-1]
                    if i-1>=0:
                        u=dp[j]
                    x[j]=l+u
                dp=x
            return x[n-1]
        return uq_tab(m,n)

           




    
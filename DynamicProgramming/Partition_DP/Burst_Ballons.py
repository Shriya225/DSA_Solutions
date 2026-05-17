# 312. Burst Balloons

# Reccurence Rel'n

def bb(a,i,j):
    if i>j:return 0
    ans=float('-inf')
    for k in range(i,j+1):
        ans=max(ans,a[i-1]*a[j+1]*a[k]+
                bb(a,i,k-1)+bb(a,k+1,j))
    return ans

# memoization...
class Solution:
    def maxCoins(self, a):
        def bb(a,i,j,dp):
            if i>j:return 0
            if dp[i][j]!=-1:return dp[i][j]
            ans=float('-inf')
            for k in range(i,j+1):
                ans=max(ans,a[i-1]*a[j+1]*a[k]+
                        bb(a,i,k-1,dp)+bb(a,k+1,j,dp))
            dp[i][j]=ans
            return ans
        a=[1]+a+[1]
        dp=[[-1]*(len(a)) for i in range(len(a))]
        return bb(a,1,len(a)-2,dp)
    
# Tabulation
class Solution:
    def maxCoins(self, a):
        a=[1]+a+[1]
        dp=[[0]*(len(a)) for i in range(len(a))]
        for i in range(len(a)-2,0,-1):
            for j in range(i,len(a)-1):
                ans=float('-inf')
                for k in range(i,j+1):
                    ans=max(ans,a[i-1]*a[j+1]*a[k]+
                            dp[i][k-1]+dp[k+1][j]
                        )
                dp[i][j]=ans
        return dp[1][-2]
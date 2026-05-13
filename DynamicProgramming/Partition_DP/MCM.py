# Matrix Chain Multiplication (GFG)

# Reccurence rel'n
def mcm(a,i,j):
    if i==j:return 0
    ans=float("inf")
    for k in range(i,j):
        ans=min(ans,a[i-1]*a[k]*a[j]+mcm(a,i,k)+mcm(a,k+1,j))
    return ans

# memoization
class Solution:
    def matrixMultiplication(self, a):
        def mcm(a,i,j,dp):
            if i==j:return 0
            if dp[i][j]!=-1:return dp[i][j]
            ans=float("inf")
            for k in range(i,j):
                ans=min(ans,a[i-1]*a[k]*a[j]+mcm(a,i,k,dp)+mcm(a,k+1,j,dp))
            dp[i][j]=ans
            return ans
        dp=[[-1]*len(a) for i in range(len(a))]
        return mcm(a,1,len(a)-1,dp)
  
# Tabulation
def mcm(a):
    dp=[[0]*len(a) for i in range(len(a))]
    for i in range(len(a)-1,0,-1):
        for j in range(i+1,len(a)):
            ans=float("inf")
            for k in range(i,j):
                ans=min(ans,a[i-1]*a[k]*a[j]+dp[i][k]+dp[k+1][j])
            dp[i][j]=ans
    return dp[1][-1]


            




